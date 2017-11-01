#include "battle.h"

#include "mind_bs.h"
#include "game_BattleShip.h"

#include "../general_lib/grid.h"
#include "../general_lib/cpoint.h"
#include "set_ships.h"

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#include <time.h>

#define TOP 0
#define BOTTOM 1
#define RIGHT 2
#define LEFT 3

bool turn = 1;

/*##### FUNZIONI PRIVATE #####*/
#define PRIVATE static

/*##### FUNZIONI PUBBLICHE #####*/
void
battle_seek_ships_uman          (BS_PLp uman, BS_PLp avversario)
{
    int x, y;
    
    while (1)
    {
        printf("Input cordinate <x,y>: ");
        scanf("%d %d", &x, &y);
        
        if (!cpoint_set(BsPl_getCord(uman), x, y))
        {
            fprintf(stderr, "Errore: conrdinate non valide!\n");
            continue;
        }
        break;
    }
}

int
battle_damege_ships_uman        (BS_PLp uman, BS_PLp avversario)
{
    char ch_casella;
    ch_casella = grid_get_point_cp(BsPl_getMare(avversario), BsPl_getCord(uman));
    
    if (ch_casella == grid_get_pat(BsPl_getMare(avversario)))
    {
        grid_set_point_cp(BsPl_getMappa(uman), BsPl_getCord(uman), MISS+48);
        return MISS;
    }
    else
    {
        int ris_damage = SetShips_damage(BsPl_getSet(avversario), ch_casella-49);
        if(ris_damage == 2)
        {
            for (int y = 0; y < grid_get_height(BsPl_getMare(avversario)); y++)
                for (int x = 0; x < grid_get_width(BsPl_getMare(avversario)); x++)
                    if (grid_get_point(BsPl_getMare(avversario), x, y) == ch_casella)
                        grid_set_point(BsPl_getMappa(uman), x, y, NAVE_AFFONDATA+49);
            
            return NAVE_AFFONDATA;
        }
        else
        if (ris_damage == 1)
        {
            grid_set_point_cp(BsPl_getMappa(uman), BsPl_getCord(uman), MISS+50);
            return NAVE_COLPITA;
        }
        else
        return MISS;
    }
}





// INTELLIGENZA ARTIFICIALE





bool
battle_seek_ships_ia            (BS_PLp ia, BS_PLp avversario)
{    
    //srand((unsigned) time(NULL));
    
    bool permiss;
    int x, y, i, k;
    
    if (battle_mind_get_NdA(BsPl_getMind(ia)))
    { // SI
        
        printf("");
        
        for (i = 0; i < 4; i++)
        {
            x = cpoint_get_x(BsPl_getCord(ia));
            y = cpoint_get_y(BsPl_getCord(ia));
            
            for(;;)
            {
                switch (i)
                {
                    case TOP:    y--; break;    case BOTTOM: y++; break;
                    case RIGHT:  x++; break;    case LEFT:   x--; break;
                }
                
                if (y < 0 || (y >= grid_get_height(BsPl_getMappa(ia))))
                    { permiss = false; break; }
                if (x < 0 || (x >= grid_get_width(BsPl_getMappa(ia))))
                    { permiss = false; break; }
                
                if (grid_get_point(BsPl_getMappa(ia), x, y) == grid_get_pat(BsPl_getMappa(ia)))
                    { permiss = true; break; }
                
                if (grid_get_point(BsPl_getMappa(ia), x, y) == '0')
                    { permiss = false; break; }
                if (grid_get_point(BsPl_getMappa(ia), x, y) == '3')
                    { permiss = false; break; }
            }
            
            if (permiss)
                battle_mind_setPermission_at(BsPl_getMind(ia), i, true);
            else battle_mind_setPermission_at(BsPl_getMind(ia), i, false);
            
            switch (i)
            {
                case TOP:
                    battle_mind_setSteps_at(BsPl_getMind(ia), i, (cpoint_get_y(BsPl_getCord(ia)) - y - 1));
                    break;
                case BOTTOM:
                    battle_mind_setSteps_at(BsPl_getMind(ia), i, (y - cpoint_get_y(BsPl_getCord(ia)) - 1));
                    break;
                case RIGHT:
                    battle_mind_setSteps_at(BsPl_getMind(ia), i, (x - cpoint_get_x(BsPl_getCord(ia)) - 1));
                    break;
                case LEFT:
                    battle_mind_setSteps_at(BsPl_getMind(ia), i, (cpoint_get_x(BsPl_getCord(ia)) - x - 1));
                    break;
            }
        }
        
        /*********************************************************************************
         *********************************************************************************
         *********************************************************************************
         *********************************************************************************
         *********************************************************************************
         *********************************************************************************/
        
        for (i = 0; i < 4; i++)
        {
            if (battle_mind_getSteps_at(BsPl_getMind(ia), i) > 0)
            {
                switch (i)
                {
                    case TOP:
                        if(!battle_mind_getPermission_at(BsPl_getMind(ia), TOP) && !battle_mind_getPermission_at(BsPl_getMind(ia), BOTTOM))
                            break;
						else if (battle_mind_getPermission_at(BsPl_getMind(ia), TOP+1))
                            return cpoint_set_y(BsPl_getCord(ia), cpoint_get_y(BsPl_getCord(ia)) + 1);
                        else return !cpoint_set(BsPl_getCord(ia), -1, -1);
                    case BOTTOM:
                        if(!battle_mind_getPermission_at(BsPl_getMind(ia), TOP) && !battle_mind_getPermission_at(BsPl_getMind(ia), BOTTOM))
                            break;
						else if(battle_mind_getPermission_at(BsPl_getMind(ia), BOTTOM-1))
                            return cpoint_set_y(BsPl_getCord(ia), cpoint_get_y(BsPl_getCord(ia)) - 1);
                        else return !cpoint_set(BsPl_getCord(ia), -1, -1);
                    case RIGHT:
                        if(!battle_mind_getPermission_at(BsPl_getMind(ia), RIGHT) && !battle_mind_getPermission_at(BsPl_getMind(ia), LEFT))
                            break;
						else if(battle_mind_getPermission_at(BsPl_getMind(ia), RIGHT+1))
                            return cpoint_set_x(BsPl_getCord(ia), cpoint_get_x(BsPl_getCord(ia)) - 1);
                        else return !cpoint_set(BsPl_getCord(ia), -1, -1);
                    case LEFT:
                        if(!battle_mind_getPermission_at(BsPl_getMind(ia), RIGHT) && !battle_mind_getPermission_at(BsPl_getMind(ia), LEFT))
                            break;
						else if(battle_mind_getPermission_at(BsPl_getMind(ia), LEFT-1))
                            return cpoint_set_x(BsPl_getCord(ia), cpoint_get_x(BsPl_getCord(ia)) + 1);
                        else return !cpoint_set(BsPl_getCord(ia), -1, -1);
                }
                break;
            }
        }
        
        
        for (i = 0, k = rand() % 4; i < 4; i++, k++)
        {
            if (k == 4) k = 0;
            
            if ((battle_mind_getPermission_at(BsPl_getMind(ia), k) == 1) && (battle_mind_getSteps_at(BsPl_getMind(ia), k) >= 0))
            {
                switch (k)
                {
                    case TOP:
                        return cpoint_set_y(BsPl_getCord(ia), cpoint_get_y(BsPl_getCord(ia)) - 1);
                    case BOTTOM:
                        return cpoint_set_y(BsPl_getCord(ia), cpoint_get_y(BsPl_getCord(ia)) + 1);
                    case RIGHT:
                        return cpoint_set_x(BsPl_getCord(ia), cpoint_get_x(BsPl_getCord(ia)) + 1);
                    case LEFT:
                        return cpoint_set_x(BsPl_getCord(ia), cpoint_get_x(BsPl_getCord(ia)) - 1);
                }
                break;
            }
        }
        
        printf("         FATTO ALGORITMO DI CERCA\n");
        
        return true;
    }
    
    // NO
    // if (queue_full(battle_mind_getQueue(BsPl_getMind(ia)))) //ho navi da affondare
    if (battle_mind_mem_isThereElmt(BsPl_getMind(ia)))
    { // SI
        
        cpoint_set(BsPl_getCord(ia), battle_mind_mem_popX(BsPl_getMind(ia)), battle_mind_mem_popY(BsPl_getMind(ia)));
        battle_mind_set_NdA(BsPl_getMind(ia), true);
        battle_seek_ships_ia (ia, avversario);
        
        printf("         HO PRESO CORDINATE DALLA MIA MEMORIA! ---> ");
    }
    else
    { // NO
        
        /* if (true) { // FORZARE LA IA AD UNA DETERMINATA CASELLA INSERITA DA INPUT DA UTENTE...
            battle_seek_ships_uman (ia, avversario);
            return true;
        } */
        
        do {
            x = rand() % cpoint_get_max_x(BsPl_getCord(ia));
            y = rand() % cpoint_get_max_y(BsPl_getCord(ia));
        } while (grid_get_point(BsPl_getMappa(ia), x, y) == '0' || grid_get_point(BsPl_getMappa(ia), x, y) == '3');
        
        printf("         HO PRESO CORDINATE A CASO!\n");
        
        return cpoint_set(BsPl_getCord(ia), x, y);
    }
    
    // sleep(1);
    
    return true;
}


/*********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 ************ SECONDA FUNZIONE PER INTELLIGENZA ARTIFICIALE **********************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************
 *********************************************************************************/


int
battle_damege_ships_ia          (BS_PLp ia, BS_PLp avversario)
{
    int x, y;
    x = cpoint_get_x(BsPl_getCord(ia));
    y = cpoint_get_y(BsPl_getCord(ia));
    
    printf("battle_damege_ships_ia().xy: %d %d\n", x, y);
    
    if( y < 0 || (y >= grid_get_height(BsPl_getMappa(ia))) ||
        x < 0 || (x >= grid_get_width(BsPl_getMappa(ia))) )
    {
        // printf("ENTERRRRRRRRRRRRR: ");
        // scanf("%d %d", &x, &y);
        // printf("prendo cordinate da memoria.\n");
        
        cpoint_set(BsPl_getCord(ia), battle_mind_mem_popX(BsPl_getMind(ia)), battle_mind_mem_popY(BsPl_getMind(ia)));
        
        battle_mind_reset(BsPl_getMind(ia));
        battle_mind_set_NdA(BsPl_getMind(ia), true); // la fa diventare true
        return MISS;
    }
    
    char ch_casella;
    ch_casella = grid_get_point_cp(BsPl_getMare(avversario), BsPl_getCord(ia));
    
    if (ch_casella == grid_get_pat(BsPl_getMare(avversario)))
    {
        grid_set_point_cp(BsPl_getMappa(ia), BsPl_getCord(ia), MISS+48);
        // -----------------------> NOT(turn);
        
        if (battle_mind_get_NdA(BsPl_getMind(ia)))
        {
            /* int x, y;
            printf("ENTERRRRRRRRRRRRR: ");
            scanf("%d %d", &x, &y); 
             cpoint_set(BsPl_getCord(ia), x, y);
             */
            
            // printf("prendo cordinate da memoria.\n");
            
            cpoint_set(BsPl_getCord(ia), battle_mind_mem_popX(BsPl_getMind(ia)), battle_mind_mem_popY(BsPl_getMind(ia)));
            
            battle_mind_reset (BsPl_getMind(ia));
            battle_mind_set_NdA(BsPl_getMind(ia), true); // la fa diventare true
        }
        
        return MISS;
    }
    else
    {
        
        int ris_damage = SetShips_damage(BsPl_getSet(avversario), ch_casella - GRAFICA_NAVI_ASCII);
        
        /* MISS 0, NAVE_COLPITA 1, NAVE_AFFONDATA 2 */
        
        /* @@@@@@@@@ NAVE COLPITA @@@@@@@@@@@ */
        if (ris_damage >= NAVE_COLPITA) {
            grid_set_point_cp(BsPl_getMappa(ia), BsPl_getCord(ia), MISS+50);
            
            // PUSH IN MEMORY, mi ricordo di aver colpito questa nave
            int shipCh = grid_get_point_cp(BsPl_getMare(avversario), BsPl_getCord(ia)) - 48;
            battle_mind_mem_pushMemory(BsPl_getMind(ia), shipCh, cpoint_get_x(BsPl_getCord(ia)), cpoint_get_y(BsPl_getCord(ia)) );
            
            battle_mind_reset(BsPl_getMind(ia));
            battle_mind_set_NdA(BsPl_getMind(ia), true); // la fa diventare true
        }
        
        
        /* @@@@@@@@@ NAVE AFFONDATA @@@@@@@@@@@ */
        if (ris_damage == NAVE_AFFONDATA) {
            for (int y = 0; y < grid_get_height(BsPl_getMare(avversario)); y++)
                for (int x = 0; x < grid_get_width(BsPl_getMare(avversario)); x++)
                    if (grid_get_point(BsPl_getMare(avversario), x, y) == ch_casella)
                        grid_set_point(BsPl_getMappa(ia), x, y, NAVE_AFFONDATA+49);
            
            battle_mind_reset(BsPl_getMind(ia));
            
            battle_mind_mem_delete(BsPl_getMind(ia), grid_get_point_cp(BsPl_getMare(avversario), BsPl_getCord(ia)) - 48);
        }
        
        
        /* @@@@@@@@@ COLPO MANCATO @@@@@@@@@@@ */
        if (ris_damage == MISS) {
            if (battle_mind_get_NdA(BsPl_getMind(ia)))
                cpoint_set(BsPl_getCord(ia), battle_mind_mem_popX(BsPl_getMind(ia)), battle_mind_mem_popY(BsPl_getMind(ia)));
        
            battle_mind_reset(BsPl_getMind(ia));
            battle_mind_set_NdA(BsPl_getMind(ia), true); // la fa diventare true
        }
        
        
        /* @@@@@@@@@ RETURN @@@@@@@@@@@ */
        return ris_damage;
        
    }
}








