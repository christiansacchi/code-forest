//
//  Rubio3x3.c
//  Rubio Another Face
//
//  Created by Christian Sacchi on 11/02/17.
//  Copyright © 2017 Christian Sacchi. All rights reserved.
//

#include "Rubio3x3.h"
#include "Mover.h"

RubikCube tri_init ()
{
    return rubikCube_init (3);
}

void tri_R   (RubikCube cubo) { rk_R(cubo); }
void tri_R2  (RubikCube cubo) { rk_R(cubo); rk_R(cubo); }
void tri_R_i (RubikCube cubo) { rk_R_i(cubo); }

move triR =     {'R', B, &tri_R, X};
move triR2 =    {'R', D, &tri_R2, X};
move triRi =    {'R', I, &tri_R_i, X};

void tri_L   (RubikCube cubo) { rk_L(cubo); }
void tri_L2  (RubikCube cubo) { rk_L(cubo); rk_L(cubo); }
void tri_L_i (RubikCube cubo) { rk_L_i(cubo); }

move triL =     {'L', B, &tri_L, X};
move triL2 =    {'L', D, &tri_L2, X};
move triLi =    {'L', I, &tri_L_i, X};

/* -=-=-=-=-=-=-=-=- */

void tri_U   (RubikCube cubo) { rk_U(cubo); }
void tri_U2  (RubikCube cubo) { rk_U(cubo); rk_U(cubo); }
void tri_U_i (RubikCube cubo) { rk_U_i(cubo); }

move triU =     {'U', B, &tri_U, Y};
move triU2 =    {'U', D, &tri_U2, Y};
move triUi =    {'U', I, &tri_U_i, Y};

void tri_D   (RubikCube cubo) { rk_D(cubo); }
void tri_D2  (RubikCube cubo) { rk_D(cubo); rk_D(cubo); }
void tri_D_i (RubikCube cubo) { rk_D_i(cubo); }

move triD =     {'D', B, &tri_D, Y};
move triD2 =    {'D', D, &tri_D2, Y};
move triDi =    {'D', I, &tri_D_i, Y};

/* -=-=-=-=-=-=-=-=- */

void tri_F   (RubikCube cubo) { rk_F(cubo); }
void tri_F2  (RubikCube cubo) { rk_F(cubo); rk_F(cubo); }
void tri_F_i (RubikCube cubo) { rk_F_i(cubo); }

move triF =     {'F', B, &tri_F, Z};
move triF2 =    {'F', D, &tri_F2, Z};
move triFi =    {'F', I, &tri_F_i, Z};

void tri_B   (RubikCube cubo) { rk_B(cubo); }
void tri_B2  (RubikCube cubo) { rk_B(cubo); rk_B(cubo); }
void tri_B_i (RubikCube cubo) { rk_B_i(cubo); }

move triB =     {'B', B, &tri_B, Z};
move triB2 =    {'B', D, &tri_B2, Z};
move triBi =    {'B', I, &tri_B_i, Z};

/* -=-=-=-=-=-=-=-=- */

void tri_M   (RubikCube cubo) { rk_M (cubo, 1); }
void tri_M2  (RubikCube cubo) { rk_M (cubo, 1); rk_M (cubo, 1); }
void tri_M_i (RubikCube cubo) { rk_M_i (cubo, 1); }

move triM =     {'M', B, &tri_M, X};
move triM2 =    {'M', D, &tri_M2, X};
move triMi =    {'M', I, &tri_M_i, X};

void tri_Lo   (RubikCube cubo) { rk_Lo (cubo, 1); }
void tri_Lo2  (RubikCube cubo) { rk_Lo (cubo, 1); rk_Lo (cubo, 1);}
void tri_Lo_i (RubikCube cubo) { rk_Lo_i (cubo, 1); }

move triLo =    {'E', B, &tri_Lo, Y};
move triLo2 =   {'E', D, &tri_Lo2, Y};
move triLoi =   {'E', I, &tri_Lo_i, Y};

void tri_La   (RubikCube cubo) { rk_La (cubo, 1); }
void tri_La2  (RubikCube cubo) { rk_La (cubo, 1); rk_La (cubo, 1);}
void tri_La_i (RubikCube cubo) { rk_La_i (cubo, 1); }

move triLa =    {'S', B, &tri_La, Z};
move triLa2 =   {'S', D, &tri_La2, Z};
move triLai =   {'S', I, &tri_La_i, Z};

/* ############### */ /* ############### */ /* ############### */

Move tri_allMoves [27] = {
    &triR, &triR2, &triRi,
    &triL, &triL2, &triLi,
    
    &triU, &triU2, &triUi,
    &triD, &triD2, &triDi,
    
    &triF, &triF2, &triFi,
    &triB, &triB2, &triBi,
    
    &triM, &triM2, &triMi,
    &triLo, &triLo2, &triLoi,
    &triLa, &triLa2, &triLai
};
unsigned int tri_allMoves_len = 27;

Move tri_scrambleMoves [18] = {
    &triR, &triR2, &triRi,
    &triL, &triL2, &triLi,
    
    &triU, &triU2, &triUi,
    &triD, &triD2, &triDi,
    
    &triF, &triF2, &triFi,
    &triB, &triB2, &triBi,
};

/* ############### */ /* ############### */ /* ############### */

int mvslst_init (move *** mvs,
                  bool _r, bool _l, bool _m,
                  bool _u, bool _d, bool _e,
                  bool _f, bool _b, bool _s,
                  unsigned int _rotation) {
    
    if (_rotation > D) _rotation = D; // (_rotation > WI)
    
    unsigned int len = 0;
    unsigned int c = 0;
    
    if (_r) len++; if (_l) len++; if (_m) len++;
    if (_u) len++; if (_d) len++; if (_e) len++;
    if (_f) len++; if (_b) len++; if (_s) len++;
    len *= (_rotation+1);
    
    Move * mvsLst = create(sizeof(Move) * len);
    // sizeof(Move) is 8 byte, couse Move is move * type
    // so here i'm allocating an array on len pinters to move_structure
    // *mvs = mvsLst;
    
    for (int i = 0; (i < tri_allMoves_len) && (c < len); i++) {
        
        if (tri_allMoves[i]->ax == X) {
            if ( _r && (tri_allMoves[i]->nome == 'R') && (tri_allMoves[i]->rotType <= _rotation) )
                mvsLst[c++] = tri_allMoves[i];
            else
            if ( _l && (tri_allMoves[i]->nome == 'L') && (tri_allMoves[i]->rotType <= _rotation) )
                mvsLst[c++] = tri_allMoves[i];
            else
            if ( _m && (tri_allMoves[i]->nome == 'M') && (tri_allMoves[i]->rotType <= _rotation) )
                mvsLst[c++] = tri_allMoves[i];
            continue;
        }
        
        if (tri_allMoves[i]->ax == Y) {
            if ( _u && (tri_allMoves[i]->nome == 'U') && (tri_allMoves[i]->rotType <= _rotation) )
                mvsLst[c++] = tri_allMoves[i];
            else
            if ( _d && (tri_allMoves[i]->nome == 'D') && (tri_allMoves[i]->rotType <= _rotation) )
                mvsLst[c++] = tri_allMoves[i];
            else
            if ( _e && (tri_allMoves[i]->nome == 'E') && (tri_allMoves[i]->rotType <= _rotation) )
                mvsLst[c++] = tri_allMoves[i];
            continue;
        }
        
        if (tri_allMoves[i]->ax == Z) {
            if ( _f && (tri_allMoves[i]->nome == 'F') && (tri_allMoves[i]->rotType <= _rotation) )
                mvsLst[c++] = tri_allMoves[i];
            else
            if ( _b && (tri_allMoves[i]->nome == 'B') && (tri_allMoves[i]->rotType <= _rotation) )
                mvsLst[c++] = tri_allMoves[i];
            else
            if ( _s && (tri_allMoves[i]->nome == 'S') && (tri_allMoves[i]->rotType <= _rotation) )
                mvsLst[c++] = tri_allMoves[i];
        }
    }
    
    // Finito con la composizione del vettore ho bisogno di dare a mvs
    
    *mvs = mvsLst;
    
    return len;
}

/* ############### */ /* ############### */ /* ############### */

Move tri_sexymove[4] = {&triR, &triU, &triRi, &triUi};
Move tri_soSexyMove[6] = {&triR, &triU, &triRi, &triUi, &triR2, &triU2};
Move tri_RUF[6] = {&triR, &triU, &triRi, &triUi, &triF, &triFi};
Move tri_RUFL[8] = {&triR, &triU, &triRi, &triL, &triUi, &triF, &triFi, &triLi };
Move tri_RUF_R2[6] = {&triR, &triU, &triRi, &triUi, &triF, &triR2};
Move tri_gonzo[4] = {&triR, &triU, &triRi, &triR2};

char simbol[5];
char * rot_type[] = {"\0", "\'\0", "2\0", "w\0", "w\'\0"};

char * move_simbol (Move m) {
    
    for (int i = 0; i < 5; simbol[i++] = 0x00);
    
    simbol[0] = m->nome;
    
    // int size = (sizeof(rot_type[m->rotType])/8);
    // printf("%s\n", rot_type[m->rotType]);
    
    for (int i = 1; i < 5; i++) {
        if (rot_type[m->rotType][i-1] == 0x00) break;
        simbol[i] = *rot_type[m->rotType];
    }
    
    return simbol;
}

void provaMover (int min, int max) {
    
    move ** mvs;
    int mvs_l;
    mvs_l = mvslst_init((move ***)&mvs, true, true, false, true, true, false, false, false, false, 0);
    
    Mover mvr = mover_init(mvs, mvs_l);
    
    RubikCube r1 = rubikCube_init(3);
    RubikCube r2 = rubikCube_init(3);
    
    /*Algo alg1 = rk_scramble (r1, *tri_scrambleMoves, 18, 25);
    for (int i = 0; i < alg1->len; i++) {
        alg1->mvs[i]->rot(r1);
        printf("%s ", move_simbol(alg1->mvs[i]));
    } putchar('\n');*/
    
    tri_R(r1); tri_F(r1); tri_L_i(r1); tri_R2(r1); tri_F_i(r1);
    tri_U_i(r1); tri_D_i(r1); tri_R_i(r1); tri_L(r1); tri_D2(r1);
    tri_F2(r1); tri_R(r1); tri_D(r1); tri_R(r1); tri_B2(r1);
    tri_R2(r1); tri_D_i(r1); tri_R_i(r1); tri_D2(r1); tri_L_i(r1);
    tri_B_i(r1); tri_F2(r1); tri_U2(r1); tri_D2(r1); tri_F_i(r1);
    
    tri_solver(r1, r2, min, max, 9999, mvr);
    
    mover_dlt(mvr);
}


void tri_solver (RubikCube cube, RubikCube c_fin,
                 const unsigned int minMvs, const unsigned int maxMvs, const unsigned int maxSltns,
                 Mover moveset) {
    
    // VAR
    //Mover_node mvr = moveset->mover;
    Mover_node mvrSLD; // Mover Node SLIDE
    Mover_link lnkSLD; // Mover Node SLIDE
    Move m;
    move * mcmp, * mcmp1, * mcmp2;
    Algo alg;
    RubikCube c_ini;
    
    unsigned int * cmbs;
    unsigned int * cmbsFll;
    
    //int lmt;
    bool full = false, real = true;
    int i, j, y, c = 0;
    int skipLOL = moveset->mover->lnk_mv_l;
    unsigned long long int alg_t, alg_a;
    
    rk_print_color(cube);
    rk_print_color(c_fin);
    
    // CODE
    for (i = minMvs; i <= maxMvs; i++) {
        
        alg_t = alg_a = 0;
        printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
        printf("Sto cercando algoritmi di lunghezza: %d\n\n", i);
        
        cmbs = create(sizeof(unsigned int) * (i+1));
        /*cmbsFll = create(sizeof(unsigned int) * (i+1));
        
        mvrSLD = moveset->mover;
        cmbsFll[0] = moveset->mover_l;
        for (y = 1; y < i; y++, mvrSLD = mvrSLD->mvrNext)
            cmbsFll[y] = mvrSLD->lnk_mv_l;*/
        
        /* -=-=-=- */
        alg = create(sizeof(algo));
        alg->mvs = create(sizeof(move) * i);
        alg->len = i;
        /* -=-=-=- */
        
        full = false;
        while (c != i) {
            
            c = 0;
            
            if (cmbs[0] >= moveset->mover_l)
                cmbs[0] = 0, cmbs[1]++;
            if (cmbs[0] >= moveset->mover_l-1)
                c++;
            
            if (cmbs[0] == 3 && cmbs[1] == 1 && cmbs[2] == 2 && cmbs[3] == 0) {
                printf("321: The Bus.\n");
            }
            
            // COMPOSIZIONE ALGORITMO
            mvrSLD = moveset->mover;
            for (y = 0; y < cmbs[0]; y++, mvrSLD = mvrSLD->mvrNext);
            alg->mvs[0] = mvrSLD->m;
            
            for (j = 1; j < i; j++) {
                
                lnkSLD = mvrSLD->lnk_mv;
                
                if (mvrSLD->isSubMove == true)
                    if (cmbs[j] == mvrSLD->lnk_mv_l) {
                        cmbs[--j]++;
                        cmbs[--j]--;
                        if (j == 0) {
                            mvrSLD = moveset->mover;
                            for (y = 0; y < cmbs[0]; y++, mvrSLD = mvrSLD->mvrNext);
                            alg->mvs[0] = mvrSLD->m;
                            j++;
                        }
                        continue;
                    }
                        
                if (cmbs[j] >= skipLOL) // mvrSLD->lnk_mv_l
                    cmbs[j] = 0, cmbs[j+1]++;
                
                if (cmbs[j] >= skipLOL-1) // mvrSLD->lnk_mv_l-1
                    c++;
                
                for (y = 0; y < cmbs[j]; y++)
                    lnkSLD = lnkSLD->next;
                
                mvrSLD = lnkSLD->link;
                alg->mvs[j] = mvrSLD->m;
            }
            
            /*if (c == i && mvrSLD->isSubMove == true) // CONDUZIONE DI USCITA...
                break;*/
            
            for (y = 0; y < i; y++)
                printf("%s ", move_simbol(alg->mvs[y]));
            printf(" -> ");
            for (y = 0; y < i; y++)
                printf("%u ", cmbs[y]);
            putchar('\n');
            // getchar();
            
            /* ANALISI ALGORITMO -=-=- */
            /*for (j = 2, real = true; j < i; j++) {
                mcmp = alg->mvs[j];
                
                if ( inSameAxes(mcmp, alg->mvs[j-1]) && isSameFace(mcmp, alg->mvs[j-2]) )
                {
                    real = false;
                    break;
                }
            }
            
            if (real) {
                for (y = 0; y < i; y++)
                    printf("%s ", move_simbol(alg->mvs[y]));
                putchar('\n');
            }*/
            
            
            /* ANALISI ALGORITMO -=-=- */
            /*if (real) {
                c_ini = cubecpy(cube);
                
                for (j = 0; j < i; j++)
                    alg->mvs[j]->rot(c_ini);
                
                if (cubecmp(c_ini, c_fin)) {
                    alg_t++;
                    printf("-=- GOOD ALG YOOH! -=- \n");
                    for (j = 0; j < i; j++)
                        printf("%s ", move_simbol(alg->mvs[j]));
                    putchar('\n');
                    printf("cube:\n"); rk_print_color(cube);
                    printf("c_ini:\n"); rk_print_color(c_ini);
                    printf("c_fin:\n"); rk_print_color(c_fin);
                    printf("-=- -=- -=- -=- -=- -=- \n");
                    cubecmp(cube, c_fin);
                }
                
                rubikCube_dlt(c_ini);
            }*/
            /* ANALISI ALGORITMO -=-=- fin*/
            
            cmbs[0]++;
        }
        
        printf("\n-- Algoritmi trovati: %llu\n", alg_t);
        printf("-- Algoritmi analizzati: %llu\n", alg_a);
        printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n");
        
        free(cmbs);
        free(alg->mvs);
        free(alg);
    }
}








