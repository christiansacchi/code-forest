
#ifndef GAME_BATTLESHIP_H
#define GAME_BATTLESHIP_H



#include <stdbool.h>
#include <time.h>
#include <stdlib.h>

#define NOT(item) ((item) = (item) ^ 0x01)

// #define N_NAVI 8
#define N_NAVI (32/sizeof(char))

#define MISS 0
#define NAVE_COLPITA 1
#define NAVE_AFFONDATA 2

#define PLAYER_1 1
#define PLAYER_2 0

#define UMAN_MIND true
#define IA_MIND false

#define GRAFICA_NAVI_ASCII 65 // Strat to 65, 'A'

// #define N_NAVI 8

typedef struct player_bs_type player_bs;
#define BS_PL player_bs
#define BS_PLp BS_PL *

BS_PLp
BsPl_create         (const int boxs_w, const int boxs_h, const bool mind);
#define BsPl_createQ(boxs,mind) BsPl_create((boxs), (boxs), (mind));

void
BsPl_destroy        (BS_PLp bs_player);

void
BsPl_pos_ships      (BS_PLp bs_player);

void
BsPl_seek_ships     (BS_PLp bs_player, BS_PLp avversario);

int
BsPl_damage_ships   (BS_PLp bs_player, BS_PLp avversario);

bool
BsPl_result         (BS_PLp bs_player, int result);

void *
BsPl_getMare        (BS_PLp bs_player);
void *
BsPl_getMappa       (BS_PLp bs_player);
void *
BsPl_getCord        (BS_PLp bs_player);
void *
BsPl_getSet         (BS_PLp bs_player);
void *
BsPl_getMind        (BS_PLp bs_player);



#endif
