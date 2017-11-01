
#ifndef POS_SHIPS_H
#define POS_SHIPS_H



#include "game_BattleShip.h"

#include <stdbool.h>

void
pos_ships_input_cord_uman       (BS_PLp bs_player);

void
pos_ships_input_cord_ia         (BS_PLp bs_player);

bool
pos_ships_position              (BS_PLp bs_player, const int dir, const int n_ship);



#endif
