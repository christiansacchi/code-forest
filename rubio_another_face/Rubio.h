//
//  Rubio.h
//  Rubio Another Face
//
//  Created by Christian Sacchi on 11/02/17.
//  Copyright © 2017 Christian Sacchi. All rights reserved.
//

#ifndef Rubio_h
#define Rubio_h

#include "miscellaneous.h"

/* ############### */ /* ############### */ /* ############### */

#define ZERO 0

#define BIANCO 1
#define GIALLO 2
#define ROSSO 3
#define ARANCIONE 4
#define VERDE 5
#define BLU 6

#define BLANK 99

#define X 1
#define Y 2
#define Z 3

#define B 0     // ""
#define I 1     // "\'"
#define D 2     // "2"
#define W 3     // "w"
#define WI 4    // "w\'"

/* ############### */ /* ############### */ /* ############### */

typedef struct rubikCube rubikCube;
typedef rubikCube * RubikCube;
typedef struct rubikFace rubikFace;
typedef rubikFace * RubikFace;

struct move {
    char nome;
    int rotType;
    void (* rot) (RubikCube);
    int ax;
};
typedef struct move move;
typedef move * Move;

struct algo {
    char * nome;
    char * txt;
    Move * mvs;
    int len;
};
typedef struct algo algo;
typedef algo * Algo;

/* ############### */ /* ############### */ /* ############### */

RubikCube rubikCube_init (const unsigned int size);
void rubikCube_dlt (RubikCube);

void rk_U   (RubikCube);
void rk_U_i (RubikCube);

void rk_D   (RubikCube);
void rk_D_i (RubikCube);

void rk_R   (RubikCube);
void rk_R_i (RubikCube);

void rk_L   (RubikCube);
void rk_L_i (RubikCube);

void rk_F   (RubikCube);
void rk_F_i (RubikCube);

void rk_B   (RubikCube);
void rk_B_i (RubikCube);

void rk_M   (RubikCube, const unsigned int l);
void rk_M_i (RubikCube, const unsigned int l);

void rk_Lo   (RubikCube, const unsigned int l);
void rk_Lo_i (RubikCube, const unsigned int l);

void rk_La   (RubikCube, const unsigned int l);
void rk_La_i (RubikCube, const unsigned int l);

/* -=-=-=-=-=-=-=-=-=-=-=-=- */

void rk_wU   (RubikCube);
void rk_wU_i (RubikCube);

void rk_wD   (RubikCube);
void rk_wD_i (RubikCube);

void rk_wR   (RubikCube);
void rk_wR_i (RubikCube);

void rk_wL   (RubikCube);
void rk_wL_i (RubikCube);

void rk_wF   (RubikCube);
void rk_wF_i (RubikCube);

void rk_wB   (RubikCube);
void rk_wB_i (RubikCube);

/* -=-=-=-=-=-=-=-=-=-=-=-=- */

void rk_x   (RubikCube);
void rk_x_i (RubikCube);
void rk_y   (RubikCube);
void rk_y_i (RubikCube);
void rk_z   (RubikCube);
void rk_z_i (RubikCube);

/* -=-=-=-=-=-=-=-=-=-=-=-=- */

Algo rk_scramble (RubikCube, Move moveset, unsigned int moveset_l, unsigned int scrmb_l);

void rk_printFace (int * face);
void rk_print   (RubikCube);
void rk_print3D (RubikCube);
void rk_print_color (RubikCube);

bool facecmp (const RubikFace, const RubikFace, const unsigned int s);
bool cubecmp (const RubikCube, const RubikCube);
RubikFace facecpy (RubikFace fsrc, const unsigned int s);
RubikCube cubecpy (RubikCube csrc);

bool isSameFace (const Move mv1, const Move mv2);
bool inSameAxes (const Move mv1, const Move mv2);

#endif /* Rubio_h */
