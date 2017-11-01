
#ifndef _GRID_H
#define _GRID_H



#include "cpoint.h"

#include <stdbool.h> // solo c99

typedef struct grid_type Grid;
#define GRID  Grid
#define GRIDp GRID *


GRIDp
grid_create         (const int width, const int height, const char pattern);
#define grid_createQ(size,pattern) grid_create((size), (size), (pattern))

void
grid_destroy        (GRIDp grid);

bool
grid_set_point      (GRIDp grid, const int x, const int y, const char ch);
char
grid_get_point      (GRIDp grid, const int x, const int y);

bool
grid_set_point_cp   (GRIDp grid, CPOINTp cpoint, const char ch);
char
grid_get_point_cp   (GRIDp grid, CPOINTp cpoint);

int
grid_get_width      (GRIDp grid);

int
grid_get_height     (GRIDp grid);

char
grid_get_pat        (GRIDp grid);

void
grid_print          (GRIDp grid);
void
grid_print_margin   (GRIDp grid);
void
grid_print_margin2   (GRIDp grid, GRIDp mappaA);
void
grid_print_margin3   (GRIDp grid, GRIDp mappaA, CPOINTp lastTarget);



#endif
