#include "game_BattleShip.h"

#include <stdio.h>

#include "pos_ships.h"
#include "battle.h"

#include "../general_lib/grid.h"
#include "../general_lib/cpoint.h"
#include "set_ships.h"
#include "mind_bs.h"

struct player_bs_type {
    GRID * mare, * mappa;
    CPOINTp cord;
    SET_SHIPSp set;
    MIND_CMPp mind;
};

/*##### FUNZIONI PRIVATE #####*/

/*##### FUNZIONI PUBBLICHE #####*/ // BsPl_create(20, 25, IA_MIND);
BS_PLp
BsPl_create         (const int boxs_w, const int boxs_h, const bool mind)
{
    BS_PLp bs_player_temp;
    bs_player_temp = malloc(sizeof(BS_PL));
    
    bs_player_temp->cord  = cpoint_create(boxs_w, boxs_h);
    bs_player_temp->mappa = grid_create(boxs_w, boxs_h, '_');
    bs_player_temp->mare  = grid_create(boxs_w, boxs_h, '_');
    bs_player_temp->set   = SetShips_create();
    
    if (mind == IA_MIND)
        bs_player_temp->mind = battle_mind_cmp_create();
    else bs_player_temp->mind = NULL;
    
    // bs_player_temp->mind = mind;
    
    return bs_player_temp;
}

void
BsPl_destroy        (BS_PLp bs_player)
{
    cpoint_destroy  (bs_player->cord);
    grid_destroy    (bs_player->mappa);
    grid_destroy    (bs_player->mare);
    SetShips_destroy(bs_player->set);
    battle_mind_cmp_destroy(bs_player->mind);
    
    free(bs_player);
}

void
BsPl_pos_ships      (BS_PLp bs_player)
{
    if (bs_player->mind == NULL)
        pos_ships_input_cord_uman(bs_player);
    else pos_ships_input_cord_ia(bs_player);
}

void
BsPl_seek_ships     (BS_PLp bs_player, BS_PLp avversario)
{
    if (bs_player->mind == NULL)
        battle_seek_ships_uman(bs_player, avversario);
    else
        while(!battle_seek_ships_ia(bs_player, avversario));
}

int
BsPl_damage_ships   (BS_PLp bs_player, BS_PLp avversario)
{
    if (bs_player->mind == NULL)
        return battle_damege_ships_uman(bs_player, avversario);
    else {
        // battle_mind_getString(bs_player->mind);
        return battle_damege_ships_ia(bs_player, avversario);
    }
    // return 1;
}

bool
BsPl_result         (BS_PLp bs_player, int result)
{
    if (bs_player->mind == NULL)
        switch (result)
    {
        case MISS:
            printf("Giocatore ha preso il mare!\n");
            return 0;
        case NAVE_COLPITA:
            printf("Giocatore ha colpito una nave!\n");
            return 1;
        case NAVE_AFFONDATA:
            printf("Giocatore ha affondato una nave!\n");
            return 1;
    }
    else
        switch (result)
    {
        case MISS:
            printf("Computer ha preso il mare!\n");
            return 0;
        case NAVE_COLPITA:
            printf("Computer ha calpito una nave!\n");
            return 1;
        case NAVE_AFFONDATA:
            printf("Computer ha affondato una nave!\n");
            return 1;
    }
    
    return 0;
}

void *
BsPl_getMare        (BS_PLp bs_player) { return bs_player->mare; }
void *
BsPl_getMappa       (BS_PLp bs_player) { return bs_player->mappa; }
void *
BsPl_getCord        (BS_PLp bs_player) { return bs_player->cord; }
void *
BsPl_getSet         (BS_PLp bs_player) { return bs_player->set; }
void *
BsPl_getMind        (BS_PLp bs_player) { return bs_player->mind; }


