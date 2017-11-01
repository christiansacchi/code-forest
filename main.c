#include "game/game_BattleShip.h"

#include "general_lib/grid.h"
#include "general_lib/cpoint.h"
#include "game/set_ships.h"

#include <stdio.h>

extern bool turn;

int main(int argc, const char ** argv)
{srand((unsigned) time(NULL));
    int contatore_turni = 0;
    
    BS_PL * christian, * computer;
    
    while (1) {
        /*christian = BsPl_createQ(15, IA_MIND);
        computer = BsPl_createQ(15, IA_MIND);*/
        christian = BsPl_create(20, 25, IA_MIND);
        computer = BsPl_create(20, 25, IA_MIND);
        
        
        BsPl_pos_ships(christian);
        BsPl_pos_ships(computer);
    
        grid_print_margin(BsPl_getMare(computer));
        
        system("clear");
        
        NOT(turn);
        while (1) {
            system("clear");
            printf("\nMAPPA COMPUTER\n");
            grid_print_margin(BsPl_getMappa(computer));
            printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
               "MARE CHRISTIAN\n");
            grid_print_margin3(BsPl_getMare(christian), BsPl_getMappa(computer), BsPl_getCord(computer));
            // grid_print_margin(BsPl_getMare(christian));
            printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
            printf("IL COMPUTER HA DETTO: %d %d\n", cpoint_get_x(BsPl_getCord(computer)), cpoint_get_y(BsPl_getCord(computer)));
        
            if (!SetShips_num_remain(BsPl_getSet(christian)) || !SetShips_num_remain(BsPl_getSet(computer)))
                break;
        
            if (turn == PLAYER_1) {
            /*BsPl_seek_ships(christian, computer);
            
            if (BsPl_result(christian, BsPl_damage_ships(christian, computer)))
                turn = PLAYER_2;
            else turn = PLAYER_2; */
                char i;
                printf("Premi un tasto per continuare: ");
                scanf("%c", &i);
                turn = PLAYER_2;
            } else {
            
                if (!SetShips_num_remain(BsPl_getSet(christian)) || !SetShips_num_remain(BsPl_getSet(computer)))
                    break;
            
                BsPl_seek_ships(computer, christian);
                
                if (BsPl_result(computer, BsPl_damage_ships(computer, christian)))
                    turn = PLAYER_1;
                else turn = PLAYER_1;
            
                contatore_turni++;
            }
        // system("clear");
    }
    // system("clear");
    
    printf("\nMAPPA COMPUTER\n");
    grid_print_margin(BsPl_getMappa(computer));
    printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
           "MARE CHRISTIAN\n");
    grid_print_margin3(BsPl_getMare(christian), BsPl_getMappa(computer), BsPl_getCord(computer));
    grid_print_margin(BsPl_getMare(christian));
    printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
    printf("IL COMPUTER HA DETTO: %d %d\n", cpoint_get_x(BsPl_getCord(computer)), cpoint_get_y(BsPl_getCord(computer)));
    
    
    if (SetShips_num_remain(BsPl_getSet(christian)))
        printf("\nChristian ha vinto!!!\n");
    else printf("\nComputer ha vinto!!!\nCONTATORE TURNI: %d\n", contatore_turni);
    
        BsPl_destroy(christian);
        BsPl_destroy(computer);
    }
    return 0;
}

/*
 CORDINATE
 
 0 0 1
 1 1 1
 2 2 1
 3 3 1
 4 4 1
 5 5 1
 6 6 1
 7 7 1
 
 0 0 1
 1 1 1
 2 2 1
 5 0 1
 6 1 1
 0 2 0
 1 3 1
 3 3 1
 */