
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
struct utente {
    
        char  *             nome;
        INFO_CONNESSIONEp   info;
        STATO_UTENTEp       flag;
};




/* #################################################
   #*#*** FUNZIONI                            ***#*#
   ################################################# */

UTENTEp   Utente    (char nome[NAME_LENGTH], INFO_CONNESSIONEp info, STATO_UTENTEp flag)
{
    UTENTEp u = calloc(1, sizeof(UTENTE));
    
    u->info = info;
    u->flag = flag;
    
    u->nome = calloc(sizeof(char), NAME_LENGTH);
    strncpy(u->nome, nome, NAME_LENGTH);
    
    return u;
}

void    Utene_canc   (UTENTEp u)
{
    free(u->nome);  free(u->info);  free(u->flag);
    u->nome = NULL; u->info = NULL; u->flag = NULL;
    free(u);  u = NULL;
}



void   utente_setNome   (UTENTEp u, char nome[NAME_LENGTH])
{
            u->nome = calloc(sizeof(char), NAME_LENGTH);
            strncpy(u->nome, nome, NAME_LENGTH);
}
void   utente_setInfo   (UTENTEp u, INFO_CONNESSIONEp info)
{
            u->info = info;
}
void   utente_setFlag   (UTENTEp u, STATO_UTENTEp flag)
{
            u->flag = flag;
}


char *    utente_getNome    (UTENTEp u)
{
                return u->nome;
}
INFO_CONNESSIONEp    utente_getInfo    (UTENTEp u)
{
                return u->info;
}
STATO_UTENTEp        utente_getFlag    (UTENTEp u)
{
                return u->flag;
}

























