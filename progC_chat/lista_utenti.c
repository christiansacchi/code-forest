/* #################################################
 #*#*** Librerie                            ***#*#
 ################################################# */
#include "chat_general_header.h"
#include "lista_utenti.h"
#include "utente.h"
#include "vector.h"


/* #################################################
 #*#*** Macro                               ***#*#
 ################################################# */
#define   none


/* #################################################
 #*#*** Strc, enum                          ***#*#
 ################################################# */
struct lista_utenti {
        VECTOR *                lista;
        __listutnt_nutenti_t    n_utenti;
};



/* #################################################
 #*#*** FUNZIONI                            ***#*#
 ################################################# */

LISTA_UTENTIp   ListaUtenti     (__listutnt_nutenti_t n_utenti)
{
    
    LISTA_UTENTIp lu = calloc(1, sizeof(LISTA_UTENTI));
    
    lu->lista = vector_create();
    
    lu->n_utenti = n_utenti;
    
    return lu;
}

void    ListaUtenti_canc        (LISTA_UTENTIp lu)
{
    vector_dlt(lu->lista);  lu->lista = NULL;
    free(lu);               lu = NULL;
}


int         listaUtenti_numUtentiMax   (LISTA_UTENTIp lu)
{
    return lu->n_utenti;
}
int         listaUtenti_numUtenti   (LISTA_UTENTIp lu)
{
    return vector_size(lu->lista);
}



int         listaUtenti_add        (LISTA_UTENTIp lu, UTENTEp u)
{
    if ( vector_size(lu->lista) == lu->n_utenti)
        return -1; // La chat è al completo di utenti
    
    vector_add(lu->lista, u);
    return 0;
}

UTENTEp     listaUtenti_getAt          (LISTA_UTENTIp lu, int at)
{
    return vector_elementAt(lu->lista, at);
}
UTENTEp     listaUtenti_getfsock      (LISTA_UTENTIp lu, int sock)
{
    int lus;
    if ( (lus = listaUenti_search(lu, sock)) == -1)
        return NULL;
    return vector_elementAt(lu->lista, lus);
}

int         listaUtenti_removeAt        (LISTA_UTENTIp lu, int at)
{
    return vector_removeAt(lu->lista, at);
}
int         listaUtenti_removefsock    (LISTA_UTENTIp lu, int sock)
{
    int lus;
    if ( (lus = listaUenti_search(lu, sock)) == -1)
        return -1;
    
    vector_removeAt(lu->lista, lus);
    return 0;
}


bool    listaUtenti_isFull    (LISTA_UTENTIp lu)
{
    if ( lu->n_utenti == vector_size(lu->lista))
        return false;       // la lista è piena
    return true;            // la lista ha spazio libero
}


int     listaUenti_search     (LISTA_UTENTIp lu, int sock)
{
    for (int i = 0; i < vector_size(lu->lista); i++)
        if (   infoConnessione_getSock( utente_getInfo(vector_elementAt(lu->lista, i)) )  == sock  )
            return i;
    
    return -1;  // non è stato trovato nessun utente corrispondente al socket
}


















