#ifndef PERCEPTRON_H
#define PERCEPTRON_H


#include <stdbool.h>

#include "ArrayLib/Array2D.h"

	
typedef struct perceptron * Perceptron_t;
typedef Perceptron_t Prctn_t;
	

Perceptron_t Perceptron_Init (double eta, unsigned int n_iter);

void Perceptron_Free (Perceptron_t self);

Perceptron_t Perceptron_Fit (Perceptron_t self, Array2D X, Array2D y);

double Perceptron_NetInput (Perceptron_t self, Array2D X, int i_sample);

int Perceptron_Predict (Perceptron_t self, Array2D X, int i_sample);


#endif /* PERCEPTRON */
