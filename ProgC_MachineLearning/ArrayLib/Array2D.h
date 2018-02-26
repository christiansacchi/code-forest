
#ifndef ARRAY_2D_H
#define ARRAY_2D_H

#include <stdbool.h>
#include "ArrayLib.h"

typedef struct array2D * Array2D;



Array2D Array2D_Init (unsigned int n_samples, unsigned int n_features);

void Array2D_Free (Array2D self);

unsigned int Array2D_Samples (Array2D self);

unsigned int Array2D_Features (Array2D self);

sample Array2D_Append (Array2D self, sample s);

sample Array2D_Index (Array2D self, unsigned int si, unsigned int fi);

sample Array2D_Get (Array2D self, unsigned int si, unsigned int fi);

sample Array2D_Set (Array2D self, unsigned int si, unsigned int fi, sample s);

void Array2D_Print (Array2D self);

void Array2D_Show (Array2D self, const char * restrict format, ...);

#endif

