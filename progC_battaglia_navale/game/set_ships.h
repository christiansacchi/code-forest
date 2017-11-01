
#ifndef SET_SHIPS_H
#define SET_SHIPS_H



#include "game_BattleShip.h"
// #define N_NAVI 8

typedef struct SetShips_type SetShips;
#define SET_SHIPS SetShips
#define SET_SHIPSp SET_SHIPS *

SET_SHIPSp
SetShips_create         (void);

void
SetShips_destroy        (SET_SHIPSp set_ships);

int
SetShips_damage         (SET_SHIPSp set_ships, int id_ship);

int
SetShips_num_tot        (SET_SHIPSp set_ships);

int
SetShips_num_remain     (SET_SHIPSp set_ships);

int
SetShips_get_ship_at    (SET_SHIPSp set_ships, const int at);



#endif
