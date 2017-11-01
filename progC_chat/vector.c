#include "vector.h"


#include <stdio.h>
#include <stdlib.h>


struct vector_type {
    int numero_elementi;            // numero elementi inseriti
    ITEM ** vector;
};


// FUNZIONI COSTRUTTRICI E DISTRUTTRICI
VECTOR * vector_create
(void)
{
    VECTOR * vector = malloc(sizeof(VECTOR));
    
    vector->numero_elementi = 0;
    vector->vector = malloc(   (vector->numero_elementi+1)*sizeof(void*) )    ;
    vector->numero_elementi = 0;
    return vector;
}

void vector_dlt
(VECTOR * vec)  { free(vec); }


// FUNZIONI PRIVATE E MACRO
#define INC_SPAZIO(x) realloc(      (x)->vector, ( ((x)->numero_elementi+1)*sizeof(void*) )      )
#define CTRL_AT(at,x) ((at) < 0) || ((at) > (x)->numero_elementi)



void vector_setNumElement
(VECTOR * vec, int num)
{   vec->numero_elementi = num;    }

// FUNZIONI GESTINE VETTORE
void vector_add
(VECTOR * vec, void * item)
{
    vec->vector[vec->numero_elementi] = item;
    vec->numero_elementi++;
    vec->vector = INC_SPAZIO(vec);
}

int vector_addAt
(VECTOR * vec, void * item, int at)
{
    if (CTRL_AT(at, vec)) return -1;
    
    for (int i = vec->numero_elementi; i > at; i--)
        vec->vector[i] = vec->vector[i-1];
    
    vec->vector[at] = item;
    vec->numero_elementi++;
    vec->vector = INC_SPAZIO(vec);
    
    return 0;
}

ITEM * vector_elementAt
(VECTOR * vec, int at)
{
    if (CTRL_AT(at, vec)) return NULL;
    return vec->vector[at];
}

int vector_removeAt
(VECTOR * vec, int at)
{
    if (CTRL_AT(at, vec)) return -1;
    
    for (int i = at; i < vec->numero_elementi; i++)
        vec->vector[i] = vec->vector[i+1];
    
    vec->numero_elementi--;
    
    return 0;
}


// FUNZIONI GENERALI
int vector_size
(VECTOR * vec) { return vec->numero_elementi; }














