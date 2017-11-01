
#ifndef chat_server_lista_utenti_h
#define chat_server_lista_utenti_h



/* #################################################
 #*#*** Librerie                            ***#*#
 ################################################# */
#include "chat_general_header.h"
#include "utente.h"

/* #################################################
 #*#*** Macro                               ***#*#
 ################################################# */
#define   none


/* #################################################
 #*#*** Strc, enum                          ***#*#
 ################################################# */
typedef struct lista_utenti  lista_utenti;
#define LISTA_UTENTI         lista_utenti
#define LISTA_UTENTIp        LISTA_UTENTI *

typedef     int                 __listutnt_nutenti_t;


/* #################################################
 #*#*** FUNZIONI                            ***#*#
 ################################################# */

LISTA_UTENTIp   ListaUtenti        (__listutnt_nutenti_t n_utenti);

void            ListaUtenti_canc   (LISTA_UTENTIp lu);


int         listaUtenti_numUtentiMax   (LISTA_UTENTIp lu);
int         listaUtenti_numUtenti      (LISTA_UTENTIp lu);


int         listaUtenti_add        (LISTA_UTENTIp lu, UTENTEp u);

UTENTEp     listaUtenti_getAt          (LISTA_UTENTIp lu, int at);
UTENTEp     listaUtenti_getfsock       (LISTA_UTENTIp lu, int sock);

int         listaUtenti_removeAt        (LISTA_UTENTIp lu, int at);
int         listaUtenti_removefsock     (LISTA_UTENTIp lu, int sock);


bool    listaUtenti_isFull    (LISTA_UTENTIp lu);


int     listaUenti_search     (LISTA_UTENTIp lu, int sock);








#endif