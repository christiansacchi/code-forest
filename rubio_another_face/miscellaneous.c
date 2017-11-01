//
//  miscellaneous.c
//  Rubio Another Face
//
//  Created by Christian Sacchi on 11/02/17.
//  Copyright © 2017 Christian Sacchi. All rights reserved.
//

#include "miscellaneous.h"

pAnonimo create(int size) {
    pAnonimo pa = malloc( size );
    memset(pa, 0, size);
    return pa;
}

unsigned long long int fattoriale(unsigned long long int n) {
    if (n == 0) return 1;
    return n * fattoriale(n - 1);
}
unsigned long long int combinazioni_con_ripetizione(unsigned long long int n, unsigned long long int k) {
    
    printf("fat 1: %llu\n", n+k-1);
    printf("fat 2: %llu\n", k);
    printf("fat 3: %llu\n", n-1);
    
    return fattoriale(n+k-1) / ( fattoriale(k)*fattoriale(n-1) );
}
