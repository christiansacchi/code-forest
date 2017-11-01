#include "grid.h"
#include "cpoint.h"

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

struct grid_type {
    int width, height;
    char pattern, * grid;
};

/*##### FUNZIONI PRIVATE #####*/
#define PRIVATE static
PRIVATE bool
in_limit_grid       (GRIDp grid, const int x, const int y)
{
    if ((x >= -1 && x < grid->width)
        &&
        (y >= -1 && y < grid->height))
        return false;
    return true;
}

/*##### FUNZIONI PUBBLICHE #####*/
GRIDp
grid_create         (const int width, const int height, const char pattern)
{
    GRIDp grid_temp;
    grid_temp = malloc(sizeof(GRID));
    
    grid_temp->grid = malloc(width * height);
    memset(grid_temp->grid, pattern, width * height);
    
    grid_temp->width = width;
    grid_temp->height = height;
    grid_temp->pattern = pattern;
    
    return grid_temp;
}

void
grid_destroy        (GRIDp grid)
{
    free(grid->grid);
    free(grid);
}

bool
grid_set_point      (GRIDp grid, const int x, const int y, const char ch)
{
    
    int pos_element = (y*grid->width) + x;
    grid->grid[pos_element] = ch;
    
    return true;
}
char
grid_get_point      (GRIDp grid, const int x, const int y)
{
    int pos_element = (y*grid->width) + x;
    // int CAZZO_DI_ELEMETO = grid->grid[pos_element];
    return grid->grid[pos_element];
}

bool
grid_set_point_cp   (GRIDp grid, CPOINTp cpoint, const char ch)
{
    int pos_element =
        (cpoint_get_y(cpoint)*grid->width) + cpoint_get_x(cpoint);
    grid->grid[pos_element] = ch;
    return true;
}
char
grid_get_point_cp   (GRIDp grid, CPOINTp cpoint)
{
    int pos_element =
        (cpoint_get_y(cpoint)*grid->width) + cpoint_get_x(cpoint);
    // int CAZZO_DI_ELEMENTO = grid->grid[pos_element];
    return grid->grid[pos_element];
}

int
grid_get_width      (GRIDp grid)
{
    return grid->width;
}

int
grid_get_height     (GRIDp grid)
{
    return grid->height;
}

char
grid_get_pat        (GRIDp grid)
{
    return grid->pattern;
}

void
grid_print          (GRIDp grid)
{
    for (int i = 0; i < (grid->width*grid->height); i++)
    {
        if ((i%grid->width == 0) && i != 0)
            putchar('\n');
        printf("%c ", *(char *)(grid->grid+i));
    }
}

void
grid_print_margin   (GRIDp grid)
{
    int i;
    
    if (grid->width > 10)
        printf("   ");
    else printf("  ");
    for (i = 0; i < grid->width; i++)
        if (grid->width > 10)
            printf("%2d ", i);
        else printf("%d ", i);
    putchar('\n');
    
    for (i = 0; i < (grid->width*grid->height); i++)
    {
        if (i%grid->width == 0)
        {
            if (i != 0) putchar('\n');
            
            if (grid->width > 10)
                printf("%2d ", i/grid->width);
            else printf("%d ", i/grid->width);
        }
        if (grid->width > 10)
            // printf("%2c ", ((*(char *)(grid->grid+i) == '0')? ('.'): (*(char *)(grid->grid+i))));
            printf("%2c ", *(char *)(grid->grid+i));
        else printf("%c ", *(char *)(grid->grid+i));
    }
}

void
grid_print_margin2   (GRIDp grid, GRIDp mappaA)
{
    int i;
    
    if (grid->width > 10)
        printf("   ");
    else printf("  ");
    for (i = 0; i < grid->width; i++)
        if (grid->width > 10)
            printf("%2d ", i);
        else printf("%d ", i);
    putchar('\n');
    
    for (i = 0; i < (grid->width*grid->height); i++)
    {
        if (i%grid->width == 0) {
            if (i != 0) putchar('\n');
            
            if (grid->width > 10)
                printf("%2d ", i/grid->width);
            else printf("%d ", i/grid->width);
        }
        
        if (grid->width > 10) {
            if ((*(char *)(mappaA->grid+i)) != '_')
                if ((*(char *)(mappaA->grid+i)) == '3')
                    printf("\e[0;46m%2c \e[0m", *(char *)(grid->grid+i));
                else printf("\e[0;45m%2c \e[0m", *(char *)(grid->grid+i));
            else printf("%2c ", *(char *)(grid->grid+i));
        }
        else {
            if ((*(char *)(mappaA->grid+i)) != '_')
                printf("\e[0;45m%c \e[0m", *(char *)(grid->grid+i));
            else printf("%c ", *(char *)(grid->grid+i));
        }
    }
}

void
grid_print_margin3   (GRIDp grid, GRIDp mappaA, CPOINTp lastTarget)
{
    int i;
    
    if (grid->width > 10)
        printf("   ");
    else printf("  ");
    for (i = 0; i < grid->width; i++)
        if (grid->width > 10)
            printf("%2d ", i);
        else printf("%d ", i);
    putchar('\n');
    
    for (i = 0; i < (grid->width*grid->height); i++)
    {
        if (i%grid->width == 0) {
            if (i != 0) putchar('\n');
            
            if (grid->width > 10)
                printf("%2d ", i/grid->width);
            else printf("%d ", i/grid->width);
        }
        
        if (i == (grid->width*cpoint_get_y(lastTarget)+cpoint_get_x(lastTarget))) {
            printf("\e[0;44m%2c \e[0m", *(char *)(grid->grid+i));
            continue;
        }
        
        if (grid->width > 10) {
            if ((*(char *)(mappaA->grid+i)) != '_')
                if ((*(char *)(mappaA->grid+i)) == '3')
                    printf("\e[0;45m%2c \e[0m", *(char *)(grid->grid+i));
                else {
                    printf("\e[0;46m%2c \e[0m", *(char *)(grid->grid+i));
                } else printf("%2c ", *(char *)(grid->grid+i));
        }
        else {
            if ((*(char *)(mappaA->grid+i)) != '_')
                printf("\e[0;46m%c \e[0m", *(char *)(grid->grid+i));
            else printf("%c ", *(char *)(grid->grid+i));
        }

    }
}


// printf("\e[1;31m%c   \e[0m", campo[I][i]);

