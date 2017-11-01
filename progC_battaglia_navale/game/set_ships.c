#include "set_ships.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// #define N_NAVI 8

struct SetShips_type {
    char set[N_NAVI];
    int num_tot_ships;
    int num_ships_remain;
};
/* struct SetShips_type {
    int * set;
    int num_tot_ships;
    int num_ships_remain;
}; */

/*##### FUNZIONI PRIVATE #####*/

/*##### FUNZIONI PUBBLICHE #####*/
SET_SHIPSp
SetShips_create         (void)
{
    char set_1x8_2x24[] =
    "\x01\x01\x01\x01\x01\x01\x01\x01"
    "\x02\x02\x02\x02\x02\x02\x02\x02"
    "\x02\x02\x02\x02\x02\x02\x02\x02"
    "\x02\x02\x02\x02\x02\x02\x02\x02"
    "\x14\x00\x00\x00\x14\x00\x00\x00";
    char set_5x4_4x6_2x20[] =
    "\x05\x05\x05\x05\x04\x04\x04\x04"
    "\x04\x04\x02\x02\x02\x02\x02\x02"
    "\x02\x02\x02\x02\x02\x02\x02\x02"
    "\x02\x02\x02\x02\x02\x02\x02\x02"
    "\x14\x00\x00\x00\x14\x00\x00\x00";
    
    SET_SHIPSp set_ships_temp;
    set_ships_temp = malloc(sizeof(SET_SHIPS));
    
    memcpy(set_ships_temp, set_5x4_4x6_2x20, sizeof(set_1x8_2x24)-1);
    
    return set_ships_temp;
}

void
SetShips_destroy        (SET_SHIPSp set_ships)
{
    free(set_ships);
}

int
SetShips_damage         (SET_SHIPSp set_ships, int id_ship)
{
    
    printf("set_ships->set[id_ship]: %d; se negativo return 0 (nave gia affondata)\n", set_ships->set[id_ship]);
    
    if(set_ships->set[id_ship])
        set_ships->set[id_ship]--;
    else return 0; // nave già affondata
    
    if (!set_ships->set[id_ship])
    {
        set_ships->num_ships_remain--;
        return 2;   // nave affondata
    }
    
    return 1; // nave colpita
}

int
SetShips_num_tot        (SET_SHIPSp set_ships)
{
    return set_ships->num_tot_ships;
}

int
SetShips_num_remain     (SET_SHIPSp set_ships)
{
    return set_ships->num_ships_remain;
}

int
SetShips_get_ship_at    (SET_SHIPSp set_ships, const int at)
{
    return set_ships->set[at];
}




