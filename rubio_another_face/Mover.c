//
//  Mover.c
//  Rubio Another Face
//
//  Created by Christian Sacchi on 18/02/17.
//  Copyright © 2017 Christian Sacchi. All rights reserved.
//

#include "Mover.h"



Mover mover_init (Move * mvs, unsigned int mvs_l) {
    
    Mover mvr;
    Mover_node rootN;
    Mover_node rootm; // Root Master
    Mover_node rotIter;
    Mover_node boxRotIter;
    Mover_link linker;
    
    mvr = create(sizeof(mover));
    
    // Creating mover stack (root)
    mvr->mover_l = mvs_l;
    for (int i = 0; i < mvs_l; i++) {
        rootN = create(sizeof(mover_node));
        rootN->isSubMove = false;
        rootN->m = mvs[i];
        rootN->mvrNext = mvr->mover;
        mvr->mover = rootN;
    }
    
    // Creating submover stack (root)
    mvr->submover_l = mvs_l;
    for (int i = 0; i < mvs_l; i++) {
        rootN = create(sizeof(mover_node));
        rootN->isSubMove = true;
        rootN->m = mvs[i];
        rootN->mvrNext = mvr->submover;
        mvr->submover = rootN;
    }
    
    /* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- */ /* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- */
    /* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- */ /* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- */
    /* PARTE 1 - Linking di submover */
    
    // Linking mover stack through
    rootN = mvr->submover;
    for (int i = 0; i < mvs_l; i++) {
        rootN->lnk_mv_l = 0;
        rootN->lnk_mv = NULL;
        
        rotIter = mvr->submover;
        rootm = mvr->mover;
        
        for (int j = 0; j < mvs_l; j++, rootm = rootm->mvrNext) {
            if (rootN->m->nome == rootm->m->nome || rootN->m->ax == rootm->m->ax)
                continue;
            linker = create(sizeof(mover_link));
            linker->link = rootm;
            linker->next = rootN->lnk_mv;
            rootN->lnk_mv = linker;
            
            rootN->lnk_mv_l += 1;
        }
        rootN = rootN->mvrNext;
    }
    
    
    /* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- */ /* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- */
    /* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- */ /* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- */
    /* PARTE 2 - Linking di mover */
    
    // Linking mover stack through
    rootN = mvr->mover;
    for (int i = 0; i < mvs_l; i++) {
        
        printf("+ %c %d\n", rootN->m->nome, rootN->m->rotType);
        
        // Init subMoveSet array
        rootN->lnk_mv_l = 0;
        rootN->lnk_mv = NULL;
        // rootN->lnk_mv = create(sizeof(mover_node)*rootN->lnk_mv_l);
        
        rotIter = mvr->mover;
        for (int j = 0; j < mvs_l; j++, rotIter = rotIter->mvrNext) {
            // NODO LV1, nomi diversi
            if (rootN->m->nome == rotIter->m->nome)
                continue;
            
            boxRotIter = rotIter;
            
            // NODO LV1, assi diversi
            // Controllo per link alla submover...
            if (rootN->m->ax == rotIter->m->ax) {
                rootm = mvr->submover;
                // Cerco in submover il link alla struttura sub
                for (int y = 0; y < mvs_l; y++, rootm = rootm->mvrNext)
                    if (rotIter->m->nome == rootm->m->nome) {
                        boxRotIter = rootm;
                        break;
                    }
            }
            
            printf("- %c %d\n", boxRotIter->m->nome, boxRotIter->m->rotType);
            
            // ADD NEW LINK TO THE STRUCT
            linker = create(sizeof(mover_link));
            linker->link = boxRotIter;
            linker->next = rootN->lnk_mv; // linking tree
            rootN->lnk_mv = linker;
            
            // Increment link counter
            rootN->lnk_mv_l += 1;
        }
        
        rootN = rootN->mvrNext;
    }
    
    return mvr;
}

void mover_dlt (Mover mvr) {
    
    printf("\n -=- Mover.c: mover_dlt() -=- \n");
    
    Mover_node rootN;
    Mover_node rootN2;
    Mover_node mvrB;
    Mover_link lnkB;
    
    int i, j;
    
    rootN = mvr->mover;
    for (i = 0; i < mvr->mover_l; i++) {
        for (j = 0; j < rootN->lnk_mv_l; j++) {
            lnkB = rootN->lnk_mv;
            rootN->lnk_mv = lnkB->next;
            free(lnkB);
        }
        rootN = rootN->mvrNext;
    }
    
    rootN2 = mvr->submover;
    for (i = 0; i < mvr->submover_l; i++) {
        for (j = 0; j < rootN2->lnk_mv_l; j++) {
            lnkB = rootN2->lnk_mv;
            rootN2->lnk_mv = lnkB->next;
            free(lnkB);
        }
        rootN2 = rootN2->mvrNext;
    }
    
    rootN = mvr->mover;
    rootN2 = mvr->submover;
    for (i = 0; i < mvr->mover_l; i++) {
        mvrB = rootN;
        rootN = rootN->mvrNext;
        free(mvrB);
        
        mvrB = rootN2;
        rootN2 = rootN2->mvrNext;
        free(mvrB);
    }
    
    free(mvr);
}













