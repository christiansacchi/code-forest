
// Librerie
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <ctype.h>

// Macro
#define size 16
#define mine 40
#define CONTROLLI (y < size && x < size && y > -1 && x > -1)
#define CONTROLLI_iI (I < size && i < size && I > -1 && i > -1)
#define CONTROLLI_iI2 (E < size && e < size && E > -1 && e > -1)
#define CONTROLLI2_iI ((campo[I][i] != '*' && !campo2[I][i]))

// Variabili Esterne
char campo[size][size];
int campo2[size][size];
bool sconfitta = false;

// Prototipi
void stampa_campo(int *mine_ipotetiche) {
    int i, I;
    printf("#mine: %2d/%2d#\n", *mine_ipotetiche, mine);
    printf("     "); for (i = 0; i < size; i++) printf("\e[4;37m  %2d\e[0m", i+1); printf("\n\n\n");
    for (I = 0; I < size; I++) {
        printf("%2d|     ", I+1);
        for (i = 0; i < size; i++) {
            switch (campo2[I][i]) {
                case 0: printf("_   "); break;
                case 1:
                    if (campo[I][i] == '_') printf("    ");
                    if (isdigit(campo[I][i]) || campo[I][i] == '*') {
                        if (campo[I][i] == '*')
                            printf("\e[1;31m%c   \e[0m", campo[I][i]);
                        else printf("\e[0;32m%c   \e[0m", campo[I][i]);
                        
                    }
                    break;
                case 2: printf("\e[0;35mP   \e[0m"); break;
            }
        }
        printf("\n\n");
    }
}
void piazzamento_numeri_stato(int X, int Y, int stato, int *mine_ipotetiche, int *mine_effettive);
void piazzamento_mine_numeri();
void posizionamento_numeri_rilevazione_mine(int x, int y);
void radar_spazzi_vuoti(int x, int y);
void ctrl_ripetizione_numero(int x, int y);


int main(void)
{
    int i, I;
    int X, Y, stato;
    int mine_ipotetiche = 0, mine_effettive = 0;
    
    for (I = 0; I < size; I++)
        for (i = 0; i < size; i++)
            campo[I][i] = '_', campo2[I][i] = 0;
    
    piazzamento_mine_numeri();
    
    do {
        stampa_campo(&mine_ipotetiche);
    
errore:
        printf("Input X-Y-stato: "); scanf("%d %d %d", &X, &Y, &stato); X--, Y--;
        if ((X > size && X < -1) && (Y > size && Y < -1) && (stato != 1 || stato != 0)) {
            printf("Errore di inserimento, reinserisci."); goto errore; }
        
        piazzamento_numeri_stato(X, Y, stato, &mine_ipotetiche, &mine_effettive);
    
    } while ( (mine_ipotetiche != mine && mine_effettive != mine) && !sconfitta );
    
    stampa_campo(&mine_ipotetiche);
    
    if (!sconfitta)
        printf("\nHAI VINTO!!!");
    else printf("\nHAI FAILATO!!!");
    
    return 0;
}

void piazzamento_numeri_stato(int X, int Y, int stato, int *mine_ipotetiche, int *mine_effettive)
{
    system("clear");
    switch (stato) {
        case true:
            if (campo[Y][X] == '_') {
                if (campo2[Y][X] == 0) radar_spazzi_vuoti(X, Y);
                if (campo2[Y][X] == 2) campo2[Y][X] = 1;
            } else
            if (isdigit(campo[Y][X])) {
                if (campo2[Y][X] == 0 || campo2[Y][X] == 2)
                    campo2[Y][X] = 1;
                else ctrl_ripetizione_numero(X, Y); // SE UGUALE A 1
            } else
            if (campo[Y][X] == '*') {
                if (campo2[Y][X] == 0 || campo2[Y][X] == 2)
                    campo2[Y][X] = 1, sconfitta = true;
            }
            break;
        case false:
            (*mine_ipotetiche)++;
            if (campo2[Y][X] == 2) campo2[Y][X] = 0;
            else
            if (campo[Y][X] == '_') {
                if (!campo2[Y][X]) campo2[Y][X] = 2;
            } else
            if (isdigit(campo[Y][X])) {
                if (!campo2[Y][X]) campo2[Y][X] = 2;
            } else
            if (campo[Y][X] == '*')
                if (!campo2[Y][X]) campo2[Y][X] = 2, mine_effettive++;
            break;
        default:
            printf("Errore di inserimento, reinserisci."); break;
    }
}

void ctrl_ripetizione_numero(int x, int y)
{
    //int X, Y;
    int i, I;
    int contatore_mine = 0, contatore_segno = 0, contatore_coppia = 0;
    
    for (I = y-1; I < y+2; I++) {
        for (i = x-1; i < x+2; i++) {
            if (CONTROLLI_iI) {
                if (campo[I][i] == '*') contatore_mine++;
                if (campo2[I][i] == 2) contatore_segno++;
                if (campo[I][i] == '*' && campo2[I][i] == 2)
                    contatore_coppia++;
            }
        }
    }
    
    printf("mine: %d;   segno: %d;   coppie: %d\n", contatore_mine, contatore_segno, contatore_coppia);
    
    if (contatore_mine == contatore_segno) {
        if (contatore_coppia == contatore_mine) {
            if (contatore_segno == 0) return;
            radar_spazzi_vuoti(x, y);
        } else
        if (contatore_coppia < contatore_mine)
            sconfitta = true;
    }
}

void piazzamento_mine_numeri()
{
    srand((unsigned) time(NULL));
    int i, I;
    char *p; p = &campo[0][0];
    int n_mine = mine, p_pos_mina;
    
    while (n_mine != 0) {
        p_pos_mina = rand() % 101;
        if (p_pos_mina > 95 && *p != '*') *p = '*', n_mine--;
        if (p == &campo[size-1][size-1] && n_mine > 0) p = &campo[0][0];
        p++;
    }
    
    for (I = 0; I < size; I++)
        for (i = 0; i < size; i++)
            if (campo[I][i] == '*')
                posizionamento_numeri_rilevazione_mine(i, I);
}

void posizionamento_numeri_rilevazione_mine(int x, int y)
{
    int i, I;
    int e, E, number;
    for (I = y-1; I < y+2; I++)
        for (i = x-1; i < x+2; i++) {
            if (I == y && i == x)
                continue;
            
            if (CONTROLLI && campo[I][i] == '_') {
                number = 0;
                for (E = I-1; E < I+2; E++)
                    for (e = i-1; e < i+2; e++) {
                        if (E == I && e == i) continue;
                        if (CONTROLLI_iI2 && campo[E][e] == '*') number++;
                    }
                if (number > 0)
                    campo[I][i] = number + 48;
            }
            
        }
}

void radar_spazzi_vuoti(int x, int y) // ROCORSIONE
{
    int i, I;
    
    if (!isdigit(campo2[y][x])) campo2[y][x] = 1;
    for (I = y-1; I < y+2; I++)
        for (i = x-1; i < x+2; i++) {
            if (I == y && i == x) continue;
                
            if (CONTROLLI_iI && CONTROLLI2_iI) {
                campo2[I][i] = 1;
                if (!isdigit(campo[I][i])) radar_spazzi_vuoti(i, I);
            }
        }
}


