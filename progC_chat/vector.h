
#ifndef VECTOR_H
#define VECTOR_H




#include <stdbool.h>

#define ITEM void

typedef struct vector_type vector;
#define VECTOR vector




VECTOR *    vector_create           (void);
void        vector_dlt              (VECTOR * vec);

void        vector_setNumElement    (VECTOR * vec, int num);


void        vector_add        (VECTOR * vec, void * item);
int         vector_addAt      (VECTOR * vec, void * item, int at);

ITEM *    vector_elementAt   (VECTOR * vec, int at);

int       vector_removeAt    (VECTOR * vec, int at);


int     vector_size         (VECTOR * vec);




#endif


