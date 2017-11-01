
#ifndef chat_server_chat_h
#define chat_server_chat_h


/* #################################################
 #*#*** Librerie                            ***#*#
 ################################################# */
#include "chat_general_header.h"
#include "lista_utenti.h"
#include "utente.h"

/* #################################################
 #*#*** Macro                               ***#*#
 ################################################# */
#define   none


/* #################################################
 #*#*** Strc, enum                          ***#*#
 ################################################# */
// CHAT_SERVER GESTIONE
struct chat {
    LISTA_UTENTIp           lista_utenti;                    // STRUTTURA LISTA UTENTI   // lista di puntatori
    
    char                    ** lista_messaggi;                  // STRUTTURA MESSAGGI
    int                     max_messaggi, n_messaggi, primo;    //
};

typedef struct chat     chat;
#define CHAT            chat
#define CHATp           CHAT *

#define CHAT_SERVER     CHAT
#define CHAT_SERVERp    CHAT_SERVER *

#define CHAT_UTENTE     CHAT
#define CHAT_UTENTEp    CHAT_UTENTE *

#define HOSTNAME_LENGTH 128

#define  GET_INFO_FROM_LIST_OF(x) utente_getInfo(  listaUtenti_getAt( c->lista_utenti, (x) )  )
#define  GET_SOCK_FROM_LIST_OF(x) infoConnessione_getSock( GET_INFO_FROM_LIST_OF( (x) ) )


/* #################################################
 #*#*** FUNZIONI                            ***#*#
 ################################################# */
// LATO SERVER
CHAT_SERVERp    chat_apri   (int porta, int utenti);
void *          gestione_connessioni (void * _chat);


// LATO CLIENT
CHAT_UTENTEp    chat_accedi (char username[NAME_LENGTH], char hostname[128], int porta);


void * scrittore (void * argv);
void * lettore (void * argv);


// ALTRO
void    chat_addUtenteFromSegmento( CHATp c, SEGMENTOp s );



#endif
