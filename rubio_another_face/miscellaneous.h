//
//  miscellaneous.h
//  Rubio Another Face
//
//  Created by Christian Sacchi on 11/02/17.
//  Copyright © 2017 Christian Sacchi. All rights reserved.
//

#ifndef miscellaneous_h
#define miscellaneous_h

#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

typedef void * pAnonimo;

pAnonimo create(int size);

unsigned long long int fattoriale (unsigned long long int n);
unsigned long long int combinazioni_con_ripetizione (unsigned long long int n, unsigned long long int k);

#endif /* miscellaneous_h */
