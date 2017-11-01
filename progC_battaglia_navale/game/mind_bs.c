#include "mind_bs.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define TOP 0
#define BOTTOM 1
#define RIGHT 2
#define LEFT 3

struct listMem_element {
    int idShip, x, y;
};
struct mind_computer_type {
    bool permission[4];
    int steps[4];
    bool NdA;
    struct listMem_element memory[N_NAVI];
    int lastElmt, maxElmt;
    // QUEUEp listMem;
};




/*********************************************************************************
 *********************************************************************************
 *********************************************************************************/
void
battle_mind_mem_pushMemory          (MIND_CMPp mind, int idShip, int x, int y)
{
    int i;
    bool pass = false;
    
    for (i = mind->lastElmt; i >= 0; i--)
        if (mind->memory[i].idShip == idShip)
            pass = true;
    
    if (pass) return;
    
    /* if (mind->lastElmt)
        if (mind->memory[mind->lastElmt-1].idShip == idShip)
            return; */
    
    mind->memory[mind->lastElmt].idShip = idShip;
    mind->memory[mind->lastElmt].x = x;
    mind->memory[mind->lastElmt++].y = y;
}

int
battle_mind_mem_popIdShip           (MIND_CMPp mind)
{
    return mind->memory[0].idShip;
}
int
battle_mind_mem_popX                (MIND_CMPp mind)
{
    return mind->memory[0].x;
}
int
battle_mind_mem_popY                (MIND_CMPp mind)
{
    return mind->memory[0].y;
}

void /* !!! */
battle_mind_mem_delete              (MIND_CMPp mind, int idShip)
{
    if (mind->memory[0].idShip == idShip)
        for (int i = 1; i < mind->lastElmt; i++)
        {
            mind->memory[i-1].idShip = mind->memory[i].idShip;
            mind->memory[i-1].x = mind->memory[i].x;
            mind->memory[i-1].y = mind->memory[i].y;
        }
    
    if (mind->lastElmt != 0)
        mind->lastElmt--;
}

bool
battle_mind_mem_isThereElmt         (MIND_CMPp mind)
{
    return (mind->lastElmt ? true : false);
}
/*********************************************************************************
 *********************************************************************************
 *********************************************************************************/




/*##### FUNZIONI PRIVATE #####*/
#define PRIVATE static

/*##### FUNZIONI PUBBLICHE #####*/
MIND_CMPp
battle_mind_cmp_create          (void)
{
    MIND_CMPp mind_temp = malloc(sizeof(MIND_CMP));
    // mind_temp->listMem = queue_create(N_NAVI, sizeof(struct listMem_element));
    mind_temp->NdA = false;
    mind_temp->lastElmt = 0;
    mind_temp->maxElmt = sizeof(mind_temp->memory)/sizeof(mind_temp->memory[0]);
    
    return mind_temp;
}

void
battle_mind_cmp_destroy         (MIND_CMPp mind)
{
    // queue_destroy(mind->listMem);
    free(mind);
}

void
battle_mind_reset               (MIND_CMPp mind)
{
    memset(mind->permission, 0, sizeof(mind->permission));
    memset(mind->steps, 0, sizeof(mind->steps));
    mind->NdA = false;
}

bool
battle_mind_get_NdA             (MIND_CMPp mind)
{
    return mind->NdA;
}
void
battle_mind_set_NdA             (MIND_CMPp mind, const bool item)
{
    mind->NdA = item;
}

bool
battle_mind_getPermission_at    (MIND_CMPp mind, const int at)
{
    return mind->permission[at];
}
void
battle_mind_setPermission_at    (MIND_CMPp mind, const int at, const bool item)
{
    mind->permission[at] = item;
}

int
battle_mind_getSteps_at         (MIND_CMPp mind, const int at)
{
    return mind->steps[at];
}
void
battle_mind_setSteps_at         (MIND_CMPp mind, const int at, const int item)
{
    mind->steps[at] = item;
}

/* void *
battle_mind_getQueue            (MIND_CMPp mind)
{
    return mind->listMem;
} */

void
battle_mind_getString       (MIND_CMPp mind)
{
    printf("       | SU |GIU | DX | SX |\n"
           "Steps  | %d  | %d  | %d  | %d  |\n"
           "Prmis  | %d  | %d  | %d  | %d  |\n"
           , mind->steps[0], mind->steps[1], mind->steps[2], mind->steps[3]
           , mind->permission[0], mind->permission[1], mind->permission[2], mind->permission[3]);
}
