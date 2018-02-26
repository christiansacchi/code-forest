


#ifndef ARRAY_LIB_H
#define ARRAY_LIB_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MACRO_DI_PROVA 46

union sample {
	int d;
	unsigned int ud;
	char c;
	bool b;
	float f;
	double lf;
	void * p;
};

typedef union sample sample;



#endif



