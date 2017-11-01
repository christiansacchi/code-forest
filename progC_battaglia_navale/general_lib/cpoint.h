
#ifndef _CPOINT_H
#define _CPOINT_H



#include <stdbool.h> // solo c99

typedef struct cpoint_type CPoint;
#define CPOINT  CPoint
#define CPOINTp CPOINT *


CPOINTp
cpoint_create       (const int max_x, const int max_y);
#define cpoint_createEQ(size) grid_create((size), (size))

void
cpoint_destroy      (CPOINTp cpoint);

bool
cpoint_set          (CPOINTp cpoint, const int x, const int y);
bool
cpoint_set_x        (CPOINTp cpoint, const int x);
bool
cpoint_set_y        (CPOINTp cpoint, const int y);

int
cpoint_get_max_x    (CPOINTp cpoint);
int
cpoint_get_max_y    (CPOINTp cpoint);

int
cpoint_get_x        (CPOINTp cpoint);
int
cpoint_get_y        (CPOINTp cpoint);

int 
cpoint_get_prec_x   (CPOINTp cpoint);
int 
cpoint_get_prec_y   (CPOINTp cpoint);
int
cpoint_get_prec2_x  (CPOINTp cpoint);
int
cpoint_get_prec2_y  (CPOINTp cpoint);



#endif
