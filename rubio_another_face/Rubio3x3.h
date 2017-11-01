//
//  Rubio3x3.h
//  Rubio Another Face
//
//  Created by Christian Sacchi on 11/02/17.
//  Copyright © 2017 Christian Sacchi. All rights reserved.
//

#ifndef Rubio3x3_h
#define Rubio3x3_h

#include "Rubio.h"
#include "Mover.h"

/* -=-=-=-=-=- */ /* -=-=-=-=-=- */ /* -=-=-=-=-=- */

RubikCube tri_init ();

void provaMover (int min, int max);

void tri_U   (RubikCube);
void tri_U2  (RubikCube);
void tri_U_i (RubikCube);

void tri_D   (RubikCube);
void tri_D2  (RubikCube);
void tri_D_i (RubikCube);

void tri_R   (RubikCube);
void tri_R2  (RubikCube);
void tri_R_i (RubikCube);

void tri_L   (RubikCube);
void tri_L2  (RubikCube);
void tri_L_i (RubikCube);

void tri_F   (RubikCube);
void tri_F2  (RubikCube);
void tri_F_i (RubikCube);

void tri_B   (RubikCube);
void tri_B2  (RubikCube);
void tri_B_i (RubikCube);

/* -=-=-=-=-=- */ /* -=-=-=-=-=- */ /* -=-=-=-=-=- */

void tri_M   (RubikCube);
void tri_M_i (RubikCube);

void tri_Lo   (RubikCube);
void tri_Lo_i (RubikCube);

void tri_La   (RubikCube);
void tri_La_i (RubikCube);

/* -=-=-=-=-=- */ /* -=-=-=-=-=- */ /* -=-=-=-=-=- */

void tri_wU   (RubikCube);
void tri_wU_i (RubikCube);

void tri_wD   (RubikCube);
void tri_wD_i (RubikCube);

void tri_wR   (RubikCube);
void tri_wR_i (RubikCube);

void tri_wL   (RubikCube);
void tri_wL_i (RubikCube);

void tri_wF   (RubikCube);
void tri_wF_i (RubikCube);

void tri_wB   (RubikCube);
void tri_wB_i (RubikCube);

/* -=-=-=-=-=- */ /* -=-=-=-=-=- */ /* -=-=-=-=-=- */

void tri_x   (RubikCube);
void tri_x_i (RubikCube);

void tri_y   (RubikCube);
void tri_y_i (RubikCube);

void tri_z   (RubikCube);
void tri_z_i (RubikCube);

/* -=-=-=-=-=- */ /* -=-=-=-=-=- */ /* -=-=-=-=-=- */

/*int mvslst_init (Move * mvs,
                 bool _r, bool _l, bool _m,
                 bool _u, bool _d, bool _e,
                 bool _f, bool _b, bool _s,
                 unsigned int _rotation);*/

void tri_solver (RubikCube cube, RubikCube c_fin,
                 const unsigned int minMvs, const unsigned int maxMvs, const unsigned int maxSltns,
                 Mover moveset);

#endif /* Rubio3x3_h */
