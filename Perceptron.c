#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#include "Perceptron.h"

struct perceptron
{	
	// Parametri
	double eta;
	unsigned int n_iter;

	// Attributi
	Array2D w_;
	Array2D errors_;
};

static void terminate(const char *message)
{
	printf("%s\n", message);
	exit(EXIT_FAILURE);
}

Perceptron_t Perceptron_Init (double eta, unsigned int n_iter)
{	
	srand(42);

	Perceptron_t self = malloc(sizeof(struct perceptron));

	if (self == NULL)
		terminate("Perceptron_Init: Perceptron non puo' essere creato.");

	self->eta = eta;
	self->n_iter = n_iter;

	self->w_ = NULL;
	self->errors_ = NULL;

	return self;	
}

void Perceptron_Free (Perceptron_t self)
{
	Array2D_Free(self->w_);
	Array2D_Free(self->errors_);
	free(self);
}


Perceptron_t Perceptron_Fit (Perceptron_t self, Array2D X, Array2D y)
{

	sample smp, target, xi;
	double update, update2;
	int errors;

	int j, ji = Array2D_Samples(X);
	int l, li = Array2D_Features(X);

	self->w_ = Array2D_Init(1 + li, 1);
	smp.d = 0;
	for (int i = 0; i < Array2D_Samples(self->w_); i++)
		Array2D_Set(self->w_, i, 0, smp);
	self->errors_ = Array2D_Init(self->n_iter, 1);

	for (int i = 0; i < self->n_iter; i++) {

		errors = 0;

		for (j = 0; j < ji; j++) {

			/* update UPDATE*/
			target = Array2D_Get(y, j, 0);

			update2 = Perceptron_Predict(self, X, j);

			update = self->eta * ((double)target.d - update2);

			printf("%d, %.3lf, %.3lf\n", target.d, update2, update);

			/* w_ UPDATE */
			for (l = 1; l < li; l++) {

				smp = Array2D_Get(self->w_, l, 0);
				xi = Array2D_Get(X, j, l);

				smp.lf += update * xi.lf;
				Array2D_Set(self->w_, l, 0, smp);
			}

			/* w_ bias UPDATE */
			smp = Array2D_Get(self->w_, 0, 0);
			smp.lf += update;
			Array2D_Set(self->w_, 0, 0, smp);

			/* errors UPDATE */
			errors += (int)(update != 0.0f);
		}

		smp.d = errors;
		Array2D_Append(self->errors_, smp);

		printf("\n\n\n");

		smp = Array2D_Get(self->w_, 0, 0);
		printf("w0: %0.4lf, ", smp.lf);
		smp = Array2D_Get(self->w_, 1, 0);
		printf("w1: %0.4lf, ", smp.lf);
		smp = Array2D_Get(self->w_, 2, 0);
		printf("w2: %0.4lf, ", smp.lf);

		printf("\n\n");
		printf("Epoch n.%d's error: %d\n\n\n", i, errors);

		getchar();
	}

	return self;
}

double Perceptron_NetInput (Perceptron_t self, Array2D X, int i_sample)
{	
	sample xi, wi;
	double dot = 0.0;

	for (int i = 1; i < Array2D_Features(X); i++) {

		xi = Array2D_Get(X, i_sample, i);
		wi = Array2D_Get(self->w_, i, 0);

		dot += xi.lf * wi.lf;
	}

	wi = Array2D_Get(self->w_, 0, 0); // Bias
	dot += wi.lf;

	// printf("dot: %.3lf - ", dot);

	return dot;
}

int Perceptron_Predict (Perceptron_t self, Array2D X, int i_sample)
{
	if (Perceptron_NetInput(self, X, i_sample) >= 0.0)
		return 1; // Iris_versicolor
	else return -1; // Iris_setosa

	return 0;
}

