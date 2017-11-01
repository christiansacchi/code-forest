//
//  main.c
//  Rubio Another Face
//
//  Created by Christian Sacchi on 11/02/17.
//  Copyright © 2017 Christian Sacchi. All rights reserved.
//

#include "Rubio.h"
#include "Rubio3x3.h"

int main(int argc, const char * argv[]) {
    
    srand((unsigned) time(NULL));
    
    RubikCube c1 = tri_init();
    
    int min, max;
    
    printf("min e max: ");
    scanf ("%d %d", &min, &max);
    
    provaMover (min, max);
    
    //tri_solver (c1, NULL, 19, 20, 100, NULL, 0);
    
    return 0;
}
