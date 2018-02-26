#include <stdio.h>
#include <stdlib.h>

#include "Array2D.h"



struct array2D
{
	sample * arr;

	unsigned int n_samples;
	unsigned int i_samples;
	unsigned int b_samples;

	unsigned int n_features;
	unsigned int i_features;
	// unsigned int b_features;

	unsigned int cels;
};


static void terminate(const char *message)
{
	printf("%s\n", message);
	exit(EXIT_FAILURE);
}


Array2D Array2D_Init (unsigned int n_samples, unsigned int n_features)
{
	Array2D self = malloc(sizeof(struct array2D));

	if (self == NULL)
		terminate("Array2D_Init: Array2D non puo' essere creato.");

	if (!n_samples || !n_features)
		terminate("Array2D_Init: n_samples/n_features ha valore non valido.");

	self->n_samples = n_samples;
	self->n_features = n_features;

	self->b_samples = self->n_samples;

	self->i_samples = 0;
	self->i_features = 0;

	self->cels = self->n_samples * self->n_features;

	self->arr = calloc(self->cels, sizeof(sample));

	if (self->arr == NULL)
		terminate("Array2D_Init: Array2D->arr non puo' essere creato.");

	return self;
}

void Array2D_Free (Array2D self)
{
	free(self->arr);
	free(self);
}

unsigned int Array2D_Samples (Array2D self)
{
	return self->n_samples;
}
unsigned int Array2D_Features (Array2D self)
{
	return self->n_features;
}

unsigned int A2D_Loc (Array2D self, unsigned int si, unsigned int fi)
{
	return (si * self->n_features) + fi;
}
unsigned int A2D_CurLoc (Array2D self)
{
	return (self->i_samples * self->n_features) + self->i_features;
}
unsigned int A2D_NextBloc (Array2D self)
{
	self->n_samples += self->b_samples;
	self->cels = self->n_samples * self->n_features;
	self->arr = realloc(self->arr, self->cels * sizeof(sample));
	if (self->arr == NULL)
		terminate("A2D_NextBloc: Array2D->arr non puo' essere ri-allocata.");
	// else printf("A2D_NextBloc: Array2D->arr ri-allocata correttamente.\n");

	return A2D_CurLoc(self);
}

sample Array2D_Append (Array2D self, sample s)
{	
	if (self->i_features >= self->n_features) {
		self->i_features = 0;
		self->i_samples++;
		if (self->i_samples >= self->n_samples) {
			A2D_NextBloc(self);
		}
	}

	int loc = A2D_CurLoc(self);
	// printf("loc: %d - ", loc);
	self->arr[loc] = s;
	
	self->i_features++;

	return self->arr[loc];
}

sample Array2D_Index (Array2D self, unsigned int si, unsigned int fi)
{
	return Array2D_Get(self, si, fi);
}
sample Array2D_Get (Array2D self, unsigned int si, unsigned int fi)
{
	int loc = A2D_Loc(self, si, fi);
	return self->arr[loc];
}
sample Array2D_Set (Array2D self, unsigned int si, unsigned int fi, sample s)
{
	int loc = A2D_Loc(self, si, fi);
	self->arr[loc] = s;
	return self->arr[loc];
}


void Array2D_Print (Array2D self)
{
	printf("Array2D => n_samples: %d; n_features: %d; cels: %d\n", self->n_samples, self->n_features, self->cels);
}


void Array2D_Show (Array2D self, const char * restrict format, ...)
{
	return;
}