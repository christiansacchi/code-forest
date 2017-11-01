//
//  Rubio.c
//  Rubio Another Face
//
//  Created by Christian Sacchi on 11/02/17.
//  Copyright © 2017 Christian Sacchi. All rights reserved.
//

#include "Rubio.h"

/* ############### */ /* ############### */ /* ############### */

#define TOP(_s,_d,_i)   ( (((_s)*(_d))+(_d)) + (_i) )
#define DX(_s,_d,_i)    ( (((_s)*(_d))-(_d)) + ((_s)*((_i)+1)) - 1 )
#define BTT(_s,_d,_i)   ( (((_s)*(_s))-1-(_i)) - (((_s)*(_d))+(_d)) )
#define SX(_s,_d,_i)    ( ((_s)*((_s)-(_i))) - (_s) - (((_s)*(_d))-(_d)) )

#define GAP_TOP(_s,_g)  ((_s)*(_g))+
#define GAP_DX(_g)      -(_g)
#define GAP_BTT(_s,_g)  -((_s)*(_g))
#define GAP_SX(_g)      (_g)+

#define FACE_RANGE(_s)      ( ((_s)*(_s))/4 )
#define DEEP_RANGE(_s, _d)  ( ((_s)-1)-(2*_d) )

/* ############### */ /* ############### */ /* ############### */

struct rubikFace {
    int color;
    int ch;
};
struct rubikCube {
    unsigned int size;
    rubikFace * up, * down;
    rubikFace * dx, * sx;
    rubikFace * front, * back;
};

/* ############### */ /* ############### */ /* ############### */

RubikCube rubikCube_init (const unsigned int size)
{
    RubikCube cube = create(sizeof(rubikCube));
    
    cube->size = size;
    
    cube->up = create(sizeof(rubikFace) * size * size);
    for (int i = 0; i < size*size; i++) {
        cube->up[i].color = BIANCO;
        cube->up[i].ch = 35;
    }
    
    cube->down = create(sizeof(rubikFace) * size * size);
    for (int i = 0; i < size*size; i++) {
        cube->down[i].color = GIALLO;
        cube->down[i].ch = 35;
    }
    
    /* -=-=-=-=- */
    
    cube->dx = create(sizeof(rubikFace) * size * size);
    for (int i = 0; i < size*size; i++) {
        cube->dx[i].color = ROSSO;
        cube->dx[i].ch = 35;
    }
    
    cube->sx = create(sizeof(rubikFace) * size * size);
    for (int i = 0; i < size*size; i++) {
        cube->sx[i].color = ARANCIONE;
        cube->sx[i].ch = 35;
    }
    
    /* -=-=-=-=- */
    
    cube->front = create(sizeof(rubikFace) * size * size);
    for (int i = 0; i < size*size; i++) {
        cube->front[i].color = VERDE;
        cube->front[i].ch = 35;
    }
    
    cube->back = create(sizeof(rubikFace) * size * size);
    for (int i = 0; i < size*size; i++) {
        cube->back[i].color = BLU;
        cube->back[i].ch = 35;
    }
    
    return cube;
}

void rubikCube_dlt (RubikCube cube) {
    free(cube->up);
    free(cube->down);
    
    free(cube->dx);
    free(cube->sx);
    
    free(cube->front);
    free(cube->back);
    
    free(cube);
}

/* ############### */ /* ############### */ /* ############### */


void rk_rotF (RubikFace rf, const unsigned int s) {
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int d = 0;
    rubikFace box;
    
    for (int i=0, j=0; i < FACE_RANGE(s); i++, j++) {
        if (j == DEEP_RANGE(s, d)) d++, j = 0;
        
        top_cord = TOP(s,d,j);
        sx_cord = SX(s,d,j);
        btt_cord = BTT(s,d,j);
        dx_cord = DX(s,d,j);
        
        box = rf[top_cord];
        rf[top_cord] = rf[sx_cord];
        rf[sx_cord] = rf[btt_cord];
        rf[btt_cord] = rf[dx_cord];
        rf[dx_cord] = box;
    }
}
void rk_rotF_i (RubikFace rf, const unsigned int s) {
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int d = 0;
    rubikFace box;
    
    for (int i=0, j=0; i < FACE_RANGE(s); i++, j++) {
        if (j == DEEP_RANGE(s, d)) d++, j = 0;
        
        top_cord = TOP(s,d,j);
        sx_cord = SX(s,d,j);
        btt_cord = BTT(s,d,j);
        dx_cord = DX(s,d,j);
        
        box = rf[top_cord];
        rf[top_cord] = rf[dx_cord];
        rf[dx_cord] = rf[btt_cord];
        rf[btt_cord] = rf[sx_cord];
        rf[sx_cord] = box;
    }
}

void rk_R   (RubikCube cube) {
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fSx = cube->up;
    RubikFace fDw = cube->front;
    RubikFace fDx = cube->down;
    rubikFace box;
    
    rk_rotF(cube->dx, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  DX(s,0,j);
        sx_cord =   DX(s,0,j);
        btt_cord =  DX(s,0,j);
        dx_cord =   SX(s,0,j);
        
        box = fUp[top_cord];
        fUp[top_cord] = fSx[sx_cord];
        fSx[sx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fDx[dx_cord];
        fDx[dx_cord] = box;
        
    }
    
}

void rk_R_i   (RubikCube cube) {
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fSx = cube->up;
    RubikFace fDw = cube->front;
    RubikFace fDx = cube->down;
    rubikFace box;
    
    rk_rotF_i(cube->dx, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  DX(s,0,j);
        sx_cord =   DX(s,0,j);
        btt_cord =  DX(s,0,j);
        dx_cord =   SX(s,0,j);
        
        box = fUp[top_cord];
        fUp[top_cord] = fDx[dx_cord];
        fDx[dx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fSx[sx_cord];
        fSx[sx_cord] = box;
        
    }
    
}

void rk_L   (RubikCube cube) {
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fDx = cube->up;
    RubikFace fDw = cube->front;
    RubikFace fSx = cube->down;
    rubikFace box;
    
    rk_rotF(cube->sx, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  DX(s,0,j) GAP_DX(s-1);
        sx_cord =   GAP_SX(s-1) SX(s,0,j);
        btt_cord =  DX(s,0,j) GAP_DX(s-1);
        dx_cord =   DX(s,0,j) GAP_DX(s-1);
        
        box = fUp[top_cord];
        fUp[top_cord] = fSx[sx_cord];
        fSx[sx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fDx[dx_cord];
        fDx[dx_cord] = box;
        
    }
}

void rk_L_i   (RubikCube cube) {
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fDx = cube->up;
    RubikFace fDw = cube->front;
    RubikFace fSx = cube->down;
    rubikFace box;
    
    rk_rotF_i(cube->sx, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  DX(s,0,j) GAP_DX(s-1);
        sx_cord =   GAP_SX(s-1) SX(s,0,j);
        btt_cord =  DX(s,0,j) GAP_DX(s-1);
        dx_cord =   DX(s,0,j) GAP_DX(s-1);
        
        box = fUp[top_cord];
        fUp[top_cord] = fDx[dx_cord];
        fDx[dx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fSx[sx_cord];
        fSx[sx_cord] = box;
        
    }
}

void rk_D  (RubikCube cube) {
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fDx = cube->sx;
    RubikFace fDw = cube->front;
    RubikFace fSx = cube->dx;
    rubikFace box;
    
    rk_rotF(cube->down, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  TOP(s,0,j);
        sx_cord =   DX(s,0,j);
        btt_cord =  BTT(s,0,j);
        dx_cord =   SX(s,0,j);
        
        box = fUp[top_cord];
        fUp[top_cord] = fSx[sx_cord];
        fSx[sx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fDx[dx_cord];
        fDx[dx_cord] = box;
    }
}
void rk_D_i (RubikCube cube) {
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fDx = cube->sx;
    RubikFace fDw = cube->front;
    RubikFace fSx = cube->dx;
    rubikFace box;
    
    rk_rotF_i(cube->down, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  TOP(s,0,j);
        sx_cord =   DX(s,0,j);
        btt_cord =  BTT(s,0,j);
        dx_cord =   SX(s,0,j);
        
        box = fUp[top_cord];
        fUp[top_cord] = fDx[dx_cord];
        fDx[dx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fSx[sx_cord];
        fSx[sx_cord] = box;
    }
}

void rk_U   (RubikCube cube) {
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fDx = cube->dx;
    RubikFace fDw = cube->front;
    RubikFace fSx = cube->sx;
    rubikFace box;
    
    rk_rotF(cube->up, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  GAP_TOP(s, s-1) TOP(s,0,j);
        sx_cord =   GAP_SX(s-1) SX(s,0,j);
        btt_cord =  BTT(s,0,j) GAP_BTT(s, s-1);
        dx_cord =   DX(s,0,j) GAP_DX(s-1);
        
        
        box = fUp[top_cord];
        fUp[top_cord] = fSx[sx_cord];
        fSx[sx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fDx[dx_cord];
        fDx[dx_cord] = box;
        
    }
}

void rk_U_i   (RubikCube cube) {
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fDx = cube->dx;
    RubikFace fDw = cube->front;
    RubikFace fSx = cube->sx;
    rubikFace box;
    
    rk_rotF_i(cube->up, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  GAP_TOP(s, s-1) TOP(s,0,j);
        sx_cord =   GAP_SX(s-1) SX(s,0,j);
        btt_cord =  BTT(s,0,j) GAP_BTT(s, s-1);
        dx_cord =   DX(s,0,j) GAP_DX(s-1);
        
        box = fUp[top_cord];
        fUp[top_cord] = fDx[dx_cord];
        fDx[dx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fSx[sx_cord];
        fSx[sx_cord] = box;
    }
}

void rk_F   (RubikCube cube) {
    
    int top_cord;
    int s = cube->size;
    RubikFace fUp = cube->up;
    RubikFace fDx = cube->dx;
    RubikFace fDw = cube->down;
    RubikFace fSx = cube->sx;
    rubikFace box;
    
    rk_rotF(cube->front, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        top_cord =  GAP_TOP(s, s-1) TOP(s,0,j);
        
        box = fUp[top_cord];
        fUp[top_cord] = fSx[top_cord];
        fSx[top_cord] = fDw[top_cord];
        fDw[top_cord] = fDx[top_cord];
        fDx[top_cord] = box;
    }
}
void rk_F_i (RubikCube cube) {
    
    int top_cord;
    int s = cube->size;
    RubikFace fUp = cube->up;
    RubikFace fDx = cube->dx;
    RubikFace fDw = cube->down;
    RubikFace fSx = cube->sx;
    rubikFace box;
    
    rk_rotF_i(cube->front, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        top_cord =  GAP_TOP(s, s-1) TOP(s,0,j);
        
        box = fUp[top_cord];
        fUp[top_cord] = fDx[top_cord];
        fDx[top_cord] = fDw[top_cord];
        fDw[top_cord] = fSx[top_cord];
        fSx[top_cord] = box;
    }
    
}

void rk_B_i   (RubikCube cube) {
    int top_cord;
    int s = cube->size;
    RubikFace fUp = cube->down;
    RubikFace fDx = cube->dx;
    RubikFace fDw = cube->up;
    RubikFace fSx = cube->sx;
    rubikFace box;
    
    rk_rotF_i(cube->back, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        top_cord =  TOP(s,0,j);
        
        box = fUp[top_cord];
        fUp[top_cord] = fDx[top_cord];
        fDx[top_cord] = fDw[top_cord];
        fDw[top_cord] = fSx[top_cord];
        fSx[top_cord] = box;
    }
}
void rk_B (RubikCube cube) {
    int top_cord;
    int s = cube->size;
    RubikFace fUp = cube->down;
    RubikFace fDx = cube->dx;
    RubikFace fDw = cube->up;
    RubikFace fSx = cube->sx;
    rubikFace box;
    
    rk_rotF(cube->back, cube->size);
    
    for (int i=0, j=0; i < s; i++, j++) {
        top_cord =  TOP(s,0,j);
        
        box = fUp[top_cord];
        fUp[top_cord] = fSx[top_cord];
        fSx[top_cord] = fDw[top_cord];
        fDw[top_cord] = fDx[top_cord];
        fDx[top_cord] = box;
    }
}

void rk_M   (RubikCube cube, const unsigned int l) {
    
    if (l == 0 || l >= cube->size)
        return;
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fSx = cube->up;
    RubikFace fDw = cube->front;
    RubikFace fDx = cube->down;
    rubikFace box;
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  DX(s,0,j) - l;
        sx_cord =   DX(s,0,j) - l;
        btt_cord =  DX(s,0,j) - l;
        dx_cord =   SX(s,0,j) + l;
        
        box = fUp[top_cord];
        fUp[top_cord] = fDx[dx_cord];
        fDx[dx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fSx[sx_cord];
        fSx[sx_cord] = box;
        
    }
}

void rk_M_i   (RubikCube cube, const unsigned int l) {
    
    if (l == 0 || l >= cube->size)
        return;
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fSx = cube->up;
    RubikFace fDw = cube->front;
    RubikFace fDx = cube->down;
    rubikFace box;
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  DX(s,0,j) - l;
        sx_cord =   DX(s,0,j) - l;
        btt_cord =  DX(s,0,j) - l;
        dx_cord =   SX(s,0,j) + l;
        
        box = fUp[top_cord];
        fUp[top_cord] = fSx[sx_cord];
        fSx[sx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fDx[dx_cord];
        fDx[dx_cord] = box;
        
    }
}

void rk_Lo_i   (RubikCube cube, const unsigned int l) {
    
    if (l == 0 || l >= cube->size)
        return;
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fDx = cube->dx;
    RubikFace fDw = cube->front;
    RubikFace fSx = cube->sx;
    rubikFace box;
    
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  GAP_TOP(s, l) TOP(s,0,j);
        sx_cord =   GAP_SX(l) SX(s,0,j);
        btt_cord =  BTT(s,0,j) GAP_BTT(s, l);
        dx_cord =   DX(s,0,j) GAP_DX(l);
        
        
        box = fUp[top_cord];
        fUp[top_cord] = fSx[sx_cord];
        fSx[sx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fDx[dx_cord];
        fDx[dx_cord] = box;
        
    }
}

void rk_Lo (RubikCube cube, const unsigned int l) {
    
    if (l == 0 || l >= cube->size)
        return;
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->back;
    RubikFace fDx = cube->dx;
    RubikFace fDw = cube->front;
    RubikFace fSx = cube->sx;
    rubikFace box;
    
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  GAP_TOP(s, l) TOP(s,0,j);
        sx_cord =   GAP_SX(l) SX(s,0,j);
        btt_cord =  BTT(s,0,j) GAP_BTT(s, l);
        dx_cord =   DX(s,0,j) GAP_DX(l);
        
        
        box = fUp[top_cord];
        fUp[top_cord] = fDx[dx_cord];
        fDx[dx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fSx[sx_cord];
        fSx[sx_cord] = box;
        
    }
}

void rk_La_i (RubikCube cube, const unsigned int l) {
    if (l == 0 || l >= cube->size)
        return;
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->up;
    RubikFace fDx = cube->dx;
    RubikFace fDw = cube->down;
    RubikFace fSx = cube->sx;
    rubikFace box;
    
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  GAP_TOP(s, l) TOP(s,0,j);
        sx_cord =   GAP_TOP(s, l) TOP(s,0,j);
        btt_cord =  GAP_TOP(s, l) TOP(s,0,j);
        dx_cord =   GAP_TOP(s, l) TOP(s,0,j);
        
        box = fUp[top_cord];
        fUp[top_cord] = fSx[sx_cord];
        fSx[sx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fDx[dx_cord];
        fDx[dx_cord] = box;
    }
}

void rk_La (RubikCube cube, const unsigned int l) {
    
    if (l == 0 || l >= cube->size)
        return;
    
    int top_cord, sx_cord, btt_cord, dx_cord;
    int s = cube->size;
    RubikFace fUp = cube->up;
    RubikFace fDx = cube->dx;
    RubikFace fDw = cube->down;
    RubikFace fSx = cube->sx;
    rubikFace box;
    
    
    for (int i=0, j=0; i < s; i++, j++) {
        
        top_cord =  GAP_TOP(s, l) TOP(s,0,j);
        sx_cord =   GAP_TOP(s, l) TOP(s,0,j);
        btt_cord =  GAP_TOP(s, l) TOP(s,0,j);
        dx_cord =   GAP_TOP(s, l) TOP(s,0,j);
        
        box = fUp[top_cord];
        fUp[top_cord] = fDx[dx_cord];
        fDx[dx_cord] = fDw[btt_cord];
        fDw[btt_cord] = fSx[sx_cord];
        fSx[sx_cord] = box;
    }
}

/* ############### */ /* ############### */ /* ############### */

void rk_print_color (RubikCube cube) {
    
    int grid_x = cube->size * 4;
    int grid_y = cube->size * 3;
    
    rubikFace grid [grid_y][grid_x];
    int x, y, s = cube->size;
    
    for (int i = 0; i < grid_y; i++)
        for (int j = 0; j < grid_x; j++) {
            grid[i][j].color = 0;
            grid[i][j].ch = 0;
        }
    
    /* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- */
    // UP
    x = s, y = s;
    //printf("UP: x -> %d; y -> %d\n", x, y);
    for (int i = 0; i < s*s; i++, x++) {
        if ((i != 0) && (i%s == 0)) y++, x = s;
        grid[y][x] = cube->up[i];
    }
    
    // DOWN
    x = (grid_x-s), y = s;
    //printf("DOWN: x -> %d; y -> %d\n", x, y);
    for (int i = 0; i < s*s; i++, x++) {
        if ((i != 0) && (i%s == 0)) y++, x = (grid_x-s);
        grid[y][x] = cube->down[i];
    }
    
    // LEFT
    x = 0, y = s;
    //printf("LEFT: x -> %d; y -> %d\n", x, y);
    for (int i = 0; i < s*s; i++, x++) {
        if ((i != 0) && (i%s == 0)) y++, x = 0;
        grid[y][x] = cube->sx[i];
    }
    
    // RIGTH
    x = s*2, y = s;
    //printf("RIGTH: x -> %d; y -> %d\n", x, y);
    for (int i = 0; i < s*s; i++, x++) {
        if ((i != 0) && (i%s == 0)) y++, x = s*2;
        grid[y][x] = cube->dx[i];
    }
    
    // BACK
    x = s, y = 0;
    //printf("BACK: x -> %d; y -> %d\n", x, y);
    for (int i = 0; i < s*s; i++, x++) {
        if ((i != 0) && (i%s == 0)) y++, x = s;
        grid[y][x] = cube->back[i];
    }
    
    // FRONT
    //printf("FRONT: x -> %d; y -> %d\n", x, y);
    x = s; y = s*2;
    for (int i = 0; i < s*s; i++, x++) {
        if ((i != 0) && (i%s == 0)) y++, x = s;
        grid[y][x] = cube->front[i];
    }
    /* -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- */
    
    
    for (int i = 0; i < grid_y; i++) {
        for (int j = 0; j < grid_x; j++)
            if (/* DISABLES CODE */ (1)) {
                switch (grid[i][j].color) {
                    case BIANCO:
                        printf(" \e[1;37m%c\e[0m", grid[i][j].ch);
                        break;
                    case GIALLO:
                        printf(" \e[1;33m%c\e[0m", grid[i][j].ch);
                        break;
                    case ROSSO:
                        printf(" \e[0;31m%c\e[0m", grid[i][j].ch);
                        break;
                    case ARANCIONE:
                        printf(" \e[0;33m%c\e[0m", grid[i][j].ch);
                        break;
                    case VERDE:
                        printf(" \e[1;32m%c\e[0m", grid[i][j].ch);
                        break;
                    case BLU:
                        printf(" \e[0;34m%c\e[0m", grid[i][j].ch);
                        break;
                    case 99:
                        printf(" .");
                        break;
                    default:
                        printf("  ");
                        break;
                }
            } else
                if (/* DISABLES CODE */ (0)) {
                    switch (grid[i][j].color) {
                        case BIANCO:
                            printf(" \e[0;37m%c\e[0m", 35);
                            break;
                        case GIALLO:
                            printf(" \e[0;33m%c\e[0m", 35);
                            break;
                        case ROSSO:
                            printf(" \e[0;31m%c\e[0m", 35);
                            break;
                        case ARANCIONE:
                            printf(" \e[0;33m%c\e[0m", 35);
                            break;
                        case VERDE:
                            printf(" \e[0;32m%c\e[0m", 35);
                            break;
                        case BLU:
                            printf(" \e[0;34m%c\e[0m", 35);
                            break;
                        case 99:
                            printf(" .");
                            break;
                        default:
                            printf("  ");
                            break;
                    }
                }
        
        printf("\n");
    }
    
    
    printf("\n");
}

/* ############### */ /* ############### */ /* ############### */

Algo rk_scramble (RubikCube cubo, Move moveset, unsigned int moveset_l, unsigned int scrmb_l) {
    
    //move alg->mvs[scrmb_l];
    
    Algo alg = create(sizeof(algo));
    alg->mvs = create(sizeof(move) * scrmb_l);
    alg->len = scrmb_l;
    
    int m;
    for (int i = 0; i < scrmb_l; i++) {
        
        m = rand() % moveset_l;
        move curMv = moveset[m];
        
        if (i >= 1) {
            move prevMv = *alg->mvs[i-1];
            if (isSameFace(&curMv, &prevMv)) {
                i--;
                continue;
            }
        }
        
        if (i >= 2) {
            move prevMv1 = *alg->mvs[i-1];
            move prevMv2 = *alg->mvs[i-2];
            
            if (inSameAxes(&curMv, &prevMv1) && isSameFace(&curMv, &prevMv2)) {
                i--;
                continue;
            }
        }
        
        alg->mvs[i] = &moveset[m];
        
    }
    
    return alg;
}

/* ############### */ /* ############### */ /* ############### */

bool facecmp (const RubikFace f1, const RubikFace f2, const unsigned int s) {
    
    int i;
    
    for (i = 0; i < s*s; i++)
        if (f1[i].color != f2[i].color)
            if (f2[i].ch != 0)
                break;
    
    if (i == s*s) return true;
    else return false;
}
bool cubecmp (const RubikCube c1, const RubikCube c2) {
    
    unsigned int s = c1->size;
    
    if ( ! facecmp(c1->up, c2->up, s))
        return false;
    
    if ( ! facecmp(c1->down, c2->down, s))
        return false;
    
    if ( ! facecmp(c1->dx, c2->dx, s))
        return false;
    
    if ( ! facecmp(c1->sx, c2->sx, s))
        return false;
    
    if ( ! facecmp(c1->front, c2->front, s))
        return false;
    
    if ( ! facecmp(c1->back, c2->back, s))
        return false;
    
    return true;
}

RubikFace facecpy (RubikFace fsrc, const unsigned int s) {
    RubikFace fest = create(sizeof(rubikFace) * s * s);
    
    for (int i = 0; i < s*s; i++) {
        fest[i].ch = fsrc[i].ch;
        fest[i].color = fsrc[i].color;
    }
    
    return fest;
}
RubikCube cubecpy (RubikCube csrc) {
    RubikCube cest = create(sizeof(rubikCube));
    cest->size = csrc->size;
    
    cest->up = facecpy(csrc->up, csrc->size);
    cest->down = facecpy(csrc->down, csrc->size);
    
    cest->dx = facecpy(csrc->dx, csrc->size);
    cest->sx = facecpy(csrc->sx, csrc->size);
    
    cest->front = facecpy(csrc->front, csrc->size);
    cest->back = facecpy(csrc->back, csrc->size);
    
    return cest;
}

bool isSameFace (const Move mv1, const Move mv2) {
    return mv1->nome == mv2->nome;
}
bool inSameAxes (const Move mv1, const Move mv2) {
    return mv1->ax == mv2->ax;
}




