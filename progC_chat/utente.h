
#ifndef chat_server_utente_h
#define chat_server_utente_h

/* #################################################
   #*#*** Librerie                            ***#*#
   ################################################# */
#include "info_connessione.h"
#include "stato_utente.h"


/* #################################################
   #*#*** Macro                               ***#*#
   ################################################# */
#define   NAME_LENGTH    20


/* #################################################
   #*#*** Strc, enum                          ***#*#
   ################################################# */
typedef struct utente  utente;
#define UTENTE         utente
#define UTENTEp        UTENTE *


/* #################################################
   #*#*** FUNZIONI                            ***#*#
   ################################################# */

UTENTEp   Utente    (char nome[NAME_LENGTH], INFO_CONNESSIONEp info, STATO_UTENTEp flag);

void    Utene_canc   (UTENTEp u);


void   utente_setNome   (UTENTEp u, char nome[NAME_LENGTH]);
void   utente_setInfo   (UTENTEp u, INFO_CONNESSIONEp info);
void   utente_setFlag   (UTENTEp u, STATO_UTENTEp flag);


char *               utente_getNome    (UTENTEp u);
INFO_CONNESSIONEp    utente_getInfo    (UTENTEp u);
STATO_UTENTEp        utente_getFlag    (UTENTEp u);


int   infoConnessione_socket    (INFO_CONNESSIONEp ic, int pfinet, int sockstream, int ipprototcp);




#endif
