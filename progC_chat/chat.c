/* #################################################
   #*#*** Librerie                            ***#*#
   ################################################# */
#include "chat.h"
#include "stato_utente.h"
#include "segmento.h"
#include "utente.h"
#include "lista_utenti.h"
#include "chat_general_header.h"


/* #################################################
 #*#*** Strutture                           ***#*#
 ################################################# */
#define MASTER_of_CHAT      "MSTRofCHAT"
#define MoC                 1 // il cratore della chat ha sempre id 1
#define MyU                 0 // ogni cliente nella sua lista personale ha sempre id 0


// CHAT_SERVER GESTIONE
/*struct chat {
    LISTA_UTENTIp           lista_utenti;                    // STRUTTURA LISTA UTENTI   // lista di puntatori
    
    char                    ** lista_messaggi;                  // STRUTTURA MESSAGGI
    int                     max_messaggi, n_messaggi, primo;    //
};*/


/* #################################################
   #*#*** Funzioni                            ***#*#
   ################################################# */
//#define  GET_INFO_FROM_LIST_OF(x) utente_getInfo(  listaUtenti_getAt( c->lista_utenti, (x) )  )
//#define  GET_SOCK_FROM_LIST_OF(x) infoConnessione_getSock( GET_INFO_FROM_LIST_OF( (x) ) )

CHAT_UTENTEp    chat_accedi (char username[NAME_LENGTH], char hostname[128], int porta)
{
    // Creazione Chat
    CHAT_UTENTEp c = calloc( 1 , sizeof(CHAT_UTENTE) );
    
    
    // Creazione Utente
    UTENTEp u = Utente(username, InfoConnessione("en1", porta, PF_INET, -1), StatoUtente(_SU__UTENTE_ON_NONE));
    infoConnessione_setIpAddr(utente_getInfo(u), hostname);
    
    
    
    if (   (infoConnessione_socket(  utente_getInfo(u), AF_INET, SOCK_STREAM, IPPROTO_TCP)  )   < 0)
    {   perror("SOCKET");  return NULL;
    }
    
    
    SEGMENTOp s = NULL;
    if ( infoConnessione_connect(utente_getInfo(u), utente_getInfo(u)) < 0) {
        // CONNESSIONE RIFIUTATA
        perror("SOCKET");
        return NULL;
    } else {
        // CONNESSIONE ACCETTATA, MA NON CONFERMATA
        
        // Ricezione messaggio conferma connessione
        s = infoConnessione_read(utente_getInfo(u));
        if (segmento_getHead(s) == ___SEGMENTO_H_YOUON_) {
            Segmento_canc(s);
            
            printf("Sei connesso alla chat.\n");
            
            
            // Invio nome utente al server
            s = Segmento(___SEGMENTO_H_UTENTELIST__, _S_1of1, NULL);
            
            char str[NAME_LENGTH];  memset(str, 0, NAME_LENGTH);
            strncpy(  str, utente_getNome(u), NAME_LENGTH  );
            
            segmento_setPayload(s, str);
            infoConnessione_write(  utente_getInfo(u), s  );
            Segmento_canc(s);
            printf("Il nome è stato inviato.\n");
            
            
            // CREZIONE LISTA UTENTI
            // Ricezione numero utenti max e numero utenti
            int num_utenti;
            
            s = infoConnessione_read(utente_getInfo(u));
            num_utenti = *((int *)(segmento_getPayload(s)));
            c->lista_utenti = ListaUtenti(num_utenti);
            listaUtenti_add(c->lista_utenti, u);    // #define MyU  0
            printf("La lista è stata creata.\n");
            
            s = infoConnessione_read(utente_getInfo(u));
            num_utenti = *((int *)(segmento_getPayload(s)));
            
            
            // Ciclo ricezione utenti del server
            for (int i = 0; i < (num_utenti-1); i++) {
                // Lettura segmento con sock e nome utenti in payload
                s = infoConnessione_read(utente_getInfo(u));
                
                /*INFO_CONNESSIONEp ic = InfoConnessione(NULL, -1, -1, -1);
                int lol = *((char *)(segmento_getPayload(s)));
                infoConnessione_setSock(ic, lol );
                
                listaUtenti_add(c->lista_utenti,  Utente((segmento_getPayload(s)+sizeof(char)), ic, NULL)  );*/
                
                chat_addUtenteFromSegmento( c, s );
                
                Segmento_canc(s);
            }
            
            printf("Preso un utente.\n");
            
            
            // SHOW UTENTI NELLA CHAT !!!!!!!!!!!
            for (int Y = 0; Y < listaUtenti_numUtenti(c->lista_utenti); Y++) {
                u = listaUtenti_getAt(c->lista_utenti, Y);
                printf("%d) %s, %d\n", Y, utente_getNome(u), infoConnessione_getSock(utente_getInfo(u)) );
            }
            
        } else {
            Segmento_canc(s);
            
            printf("Non sei conneso alla chat.");
        }
    }
    
    
    return c;
}

void     chat_chiudi    (CHATp chat);



void    chat_addUtenteFromSegmento( CHATp c, SEGMENTOp s )
{
    
    //s = infoConnessione_read( GET_INFO_FROM_LIST_OF(MyU) );
    
    INFO_CONNESSIONEp ic = InfoConnessione(NULL, -1, -1, -1);
    int lol = *((char *)(segmento_getPayload(s)));
    infoConnessione_setSock(ic, lol );
    
    listaUtenti_add(c->lista_utenti,  Utente((segmento_getPayload(s)+sizeof(char)), ic, NULL)  );
    
    //Segmento_canc(s);

}




void * scrittore (void * _chat)
{
    CHAT_SERVERp c = _chat;
    
    char str[_SEGMENTO_PAYLOAD_LENGTH-1];
    SEGMENTOp s = NULL;
    
    loop {
        printf("> "); read_line(str, sizeof(str));
        s = Segmento(1, _S_1of1, str);
        infoConnessione_write(GET_INFO_FROM_LIST_OF(0), s);
        Segmento_canc(s);
    }
    
    return NULL;
}

void * lettore (void * _chat)
{
    CHAT_SERVERp c = _chat;
    SEGMENTOp s = NULL;
    
    loop {
        
        if ( (s = infoConnessione_read( GET_INFO_FROM_LIST_OF(0) )) == NULL ) {
            perror("s == null");
            continue;
        }
        
        
        int sHead = segmento_getHead(s);
        
        if ( (sHead >= ___SEGMENTO_HEAD_UTENTE1__) && (sHead <= ___SEGMENTO_HEAD_UTENTE150__) ) {
            
            //char sock[1];
            //strncpy( sock , segmento_getPayload(s), sizeof(char));
            
            printf("\e[0;46m%s: %s\e[0m\n",
                   utente_getNome( listaUtenti_getfsock(c->lista_utenti, segmento_getHead(s)) ),
                   segmento_getPayload(s));
            
            for (int i = 0; i < 100000; i++);
            
            // segmento_show(s);
            
        } else if (sHead == ___SEGMENTO_H_CLOSE_) {
            
            printf("Chiudo connessione con utente sock");
            
        } else if (sHead == ___SEGMENTO_H_UTENTELIST__) {
            
            chat_addUtenteFromSegmento(c, s);
            
        }
        
        
        Segmento_canc(s);
        
    }
    
    return NULL;
}












