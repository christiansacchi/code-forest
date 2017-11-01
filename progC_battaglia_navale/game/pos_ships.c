#include "pos_ships.h"

#include "../general_lib/grid.h"
#include "../general_lib/cpoint.h"
#include "set_ships.h"

#include <stdio.h>

/*##### FUNZIONI PRIVATE #####*/

/*##### FUNZIONI PUBBLICHE #####*/
void
pos_ships_input_cord_uman       (BS_PLp bs_player)
{
    int x, y, dir, i;
    
    for (i = 0; i < SetShips_num_tot(BsPl_getSet(bs_player)); i++)
    {
        while (1)
        {
            printf("Input cordinate <x,y,dir>: ");
            scanf("%d %d %d", &x, &y, &dir);
            
            if (!cpoint_set(BsPl_getCord(bs_player), x, y))
            {
                fprintf(stderr, "Errore: conrdinate non valido!\n");
                continue;
            }
            
            if (!pos_ships_position(bs_player, dir, i))
            {
                fprintf(stderr, "Errore: impossibili inserire nave!\n");
                i--;
            }
            
            // grid_print(BsPl_getMare(bs_player));
            
            break;
        }
    }
}

void
pos_ships_input_cord_ia         (BS_PLp bs_player)
{
    //srand((unsigned) time(NULL));
    
    int x, y, dir = 0, i;
    
    for (i = 0; i < SetShips_num_tot(BsPl_getSet(bs_player)); i++)
    {
        while (1)
        {
            x = rand() % cpoint_get_max_x(BsPl_getCord(bs_player));
            y = rand() % cpoint_get_max_y(BsPl_getCord(bs_player));
            dir = rand() % 2;
            
            if ((!cpoint_set(BsPl_getCord(bs_player), x, y))
                ||
                (grid_get_point(BsPl_getMare(bs_player), x, y) != grid_get_pat(BsPl_getMare(bs_player))))
                continue;
            
            if (!pos_ships_position(bs_player, dir, i))
                i--;
            
            break;
        }
    }
}

bool
pos_ships_position              (BS_PLp bs_player, const int dir, const int n_ship)
{
    int i, cord_y, cord_x;
    
    switch (dir)
    {
        case true: // ORIZZONTALE
        {
            cord_x = cpoint_get_x(BsPl_getCord(bs_player));
            
            if (SetShips_get_ship_at(BsPl_getSet(bs_player), n_ship)
                > (cpoint_get_max_x(BsPl_getCord(bs_player))-cord_x))
                return false;
            
            cord_y = cpoint_get_y(BsPl_getCord(bs_player));
            
            for (i = cord_x;
                 i < (cord_x + SetShips_get_ship_at(BsPl_getSet(bs_player), n_ship));)
            {
                if (grid_get_point(BsPl_getMare(bs_player), i, cord_y) != grid_get_pat(BsPl_getMare(bs_player)))
                {
                    i--;
                    while (i >= cord_x)
                        grid_set_point(BsPl_getMare(bs_player), i--, cord_y, grid_get_pat(BsPl_getMare(bs_player)));
                    return false;
                }
                // grid_set_point(bs_player->mare, i++, cord_y, SetShips_get_ship_at(bs_player->set, n_ship)+48);
                grid_set_point(BsPl_getMare(bs_player), i++, cord_y, n_ship+GRAFICA_NAVI_ASCII);
            }
        }
        break;
            
        case false: // VERTICALE
        {
            cord_y = cpoint_get_y(BsPl_getCord(bs_player));
            
            if (SetShips_get_ship_at(BsPl_getSet(bs_player), n_ship)
                > (cpoint_get_max_y(BsPl_getCord(bs_player))-cord_y))
                return false;
            
            cord_x = cpoint_get_x(BsPl_getCord(bs_player));
            
            for (i = cpoint_get_y(BsPl_getCord(bs_player));
                 i < (cord_y + SetShips_get_ship_at(BsPl_getSet(bs_player), n_ship));)
            {
                if (grid_get_point(BsPl_getMare(bs_player), cord_x, i) != grid_get_pat(BsPl_getMare(bs_player)))
                {
                    i--;
                    while (i >= cord_y)
                        grid_set_point(BsPl_getMare(bs_player), cord_x, i--, grid_get_pat(BsPl_getMare(bs_player)));
                    return false;
                }
                // grid_set_point(bs_player->mare, cord_x, i++, SetShips_get_ship_at(bs_player->set, n_ship)+48);
                grid_set_point(BsPl_getMare(bs_player), cord_x, i++, n_ship+GRAFICA_NAVI_ASCII);
            }
        }
        break;
    }
    
    return true;
}













