//
//  Mover.h
//  Rubio Another Face
//
//  Created by Christian Sacchi on 18/02/17.
//  Copyright © 2017 Christian Sacchi. All rights reserved.
//

#ifndef Mover_h
#define Mover_h

#include "Rubio.h"

typedef struct mover_link mover_link;
typedef mover_link * Mover_link;

typedef struct mover_node mover_node;
typedef mover_node * Mover_node;

typedef struct mover mover;
typedef mover * Mover;


struct mover_node {
    Move m;
    
    bool isSubMove;
    struct mover_link * lnk_mv;
    unsigned int lnk_mv_l;
    
    struct mover_node * mvrNext;
};

struct mover {
    struct mover_node * mover;
    unsigned int mover_l;
    struct mover_node * submover;
    unsigned int submover_l;
};

struct mover_link {
    struct mover_link * prev;
    struct mover_node * link;
    struct mover_link * next;
};


Mover mover_init (Move * mvs, unsigned int mvs_l);
void mover_dlt (Mover mvr);

#endif /* Mover_h */
