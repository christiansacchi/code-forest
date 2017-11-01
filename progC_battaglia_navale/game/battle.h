
#ifndef BATTLE_H
#define BATTLE_H

#include "game_BattleShip.h"

void
battle_seek_ships_uman      (BS_PLp uman, BS_PLp avversario);

int
battle_damege_ships_uman    (BS_PLp uman, BS_PLp avversario);

bool
battle_seek_ships_ia        (BS_PLp ia, BS_PLp avversario);

int
battle_damege_ships_ia      (BS_PLp ia, BS_PLp avversario);

 

#endif

/* MARE
 *
 * 0 mare
 * 1 nave
 * 2 nave colpita
 * 3 nave affondata
 */
/* MAPPA
 *
 * 0 mare
 * 1 miss
 * 2 colpita
 * 3 affondata
 */