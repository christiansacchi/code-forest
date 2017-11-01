#include "cpoint.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct cpoint_type {   // andrà nel .c
    int MaxX, MaxY;
    int x, y;
    int precX, precY;
    int precX2, precY2;
};

/*##### FUNZIONI PRIVATE #####*/
#define PRIVATE static

/*##### FUNZIONI PUBBLICHE #####*/
CPOINTp
cpoint_create       (const int max_x, const int max_y)
{
    CPOINTp cpoint_temp;
    cpoint_temp = malloc(sizeof(CPOINT));
    
    memset(cpoint_temp, 0, sizeof(CPOINT));
           
    cpoint_temp->MaxX = max_x;
    cpoint_temp->MaxY = max_y;
    
    return cpoint_temp;
}

void
cpoint_destroy      (CPOINTp cpoint)
{
    free(cpoint);
}

bool
cpoint_set          (CPOINTp cpoint, const int x, const int y)
{
    if ((x > cpoint->MaxX-1 || x < 0)
        &&
        (y > cpoint->MaxY-1 || y < 0))
        return false;
    
    /* cpoint->precX2 = cpoint->precX;
    cpoint->precX = cpoint->x; */
    cpoint->x = x;
    /* cpoint->precY2 = cpoint->precY;
    cpoint->precY = cpoint->y; */
    cpoint->y = y;
    
    return true;
}
bool
cpoint_set_x        (CPOINTp cpoint, const int x)
{
    if (x > cpoint->MaxX || x < 0)
        return false;
    
    cpoint->precX2 = cpoint->precX;
    cpoint->precX = cpoint->x;
    cpoint->x = x;
    
    return true;
}
bool
cpoint_set_y        (CPOINTp cpoint, const int y)
{
    if (y > cpoint->MaxX || y < 0)
        return false;
    
    cpoint->precY2 = cpoint->precY;
    cpoint->precY = cpoint->y;
    cpoint->y = y;
    
    return true;
}

int
cpoint_get_max_x    (CPOINTp cpoint) { return cpoint->MaxX; }
int
cpoint_get_max_y    (CPOINTp cpoint) { return cpoint->MaxY; }

int
cpoint_get_x        (CPOINTp cpoint) { return cpoint->x; }
int
cpoint_get_y        (CPOINTp cpoint) { return cpoint->y; }

int
cpoint_get_prec_x   (CPOINTp cpoint) { return cpoint->precX; }
int
cpoint_get_prec_y   (CPOINTp cpoint) { return cpoint->precY; }
int
cpoint_get_prec2_x  (CPOINTp cpoint) { return cpoint->precX2; }
int
cpoint_get_prec2_y  (CPOINTp cpoint) { return cpoint->precY2; }



