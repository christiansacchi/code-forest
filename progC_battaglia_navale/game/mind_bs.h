
#ifndef MIND_BS_H
#define MIND_BS_H



#include "game_BattleShip.h"
// #include "../../queue.h"

#include <stdbool.h>

typedef struct mind_computer_type mind_computer;
#define MIND_CMP mind_computer
#define MIND_CMPp MIND_CMP *


/*********************************************************************************
 *********************************************************************************
 *********************************************************************************/
void
battle_mind_mem_pushMemory          (MIND_CMPp mind, int idShip, int x, int y);

int
battle_mind_mem_popIdShip           (MIND_CMPp mind);
int
battle_mind_mem_popX                (MIND_CMPp mind);
int
battle_mind_mem_popY                (MIND_CMPp mind);

void
battle_mind_mem_delete              (MIND_CMPp mind, int idShip);

bool
battle_mind_mem_isThereElmt         (MIND_CMPp mind);

/*********************************************************************************
 *********************************************************************************
 *********************************************************************************/
MIND_CMPp
battle_mind_cmp_create          (void);

void
battle_mind_cmp_destroy         (MIND_CMPp mind);

void
battle_mind_reset               (MIND_CMPp mind);

bool
battle_mind_get_NdA             (MIND_CMPp mind);
void
battle_mind_set_NdA             (MIND_CMPp mind, const bool item);

bool
battle_mind_getPermission_at    (MIND_CMPp mind, const int at);
void
battle_mind_setPermission_at    (MIND_CMPp mind, const int at, const bool item);

int
battle_mind_getSteps_at         (MIND_CMPp mind, const int at);
void
battle_mind_setSteps_at         (MIND_CMPp mind, const int at, const int item);

void *
battle_mind_getQueue            (MIND_CMPp mind);

void
battle_mind_getString           (MIND_CMPp mind);



#endif
