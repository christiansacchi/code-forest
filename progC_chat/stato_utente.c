
/* #################################################
   #*#*** Librerie                            ***#*#
   ################################################# */
#include "chat_general_header.h"

#include "stato_utente.h"



/* #################################################
 #*#*** Macro                               ***#*#
 ################################################# */
#define _none



/* #################################################
   #*#*** Strc, enum                          ***#*#
   ################################################# */
struct stato_utente {
        __statutente_grado_t         grado;
        __statutente_stato_t         stato;
        __statutente_blocco_t        blocco;
};






/* #################################################
   #*#*** FUNZIONI                            ***#*#
   ################################################# */

STATO_UTENTEp   StatoUtente     (__statutente_grado_t grado, __statutente_stato_t stato, __statutente_blocco_t blocco)
{
                    STATO_UTENTEp su = calloc(1, sizeof(STATO_UTENTE));
                    if (su == NULL) perror("CALLOC");
    
                    su->grado   = grado;
                    su->stato   = stato;
                    su->blocco  = blocco;
    
                    return su;
}
STATO_UTENTEp   StatoUtente_grado  (__statutente_grado_t grado)
{
                    return  StatoUtente(grado, ___STATUTENTE_STATO_ON__, ___STATUTENTE_BLOCCO_NONE__);
}

void    StatoUtente_canc   (STATO_UTENTEp su)
{
                    free(su);
                    su = NULL;
}


void   statoUtente_setGrado   (STATO_UTENTEp su, __statutente_grado_t grado)
{
                    su->grado = grado;
}
void   statoUtente_setStato   (STATO_UTENTEp su, __statutente_stato_t stato)
{
                    su->stato = stato;
}
void   statoUtente_setBlocco  (STATO_UTENTEp su, __statutente_blocco_t blocco)
{
                    su->blocco = blocco;
}


__statutente_grado_t    statoUtente_getGrado    (STATO_UTENTEp su)
{
                    return su->grado;
}
__statutente_stato_t    statoUtente_getStato    (STATO_UTENTEp su)
{
                    return su->stato;
}
__statutente_blocco_t   statoUtente_getBlocco   (STATO_UTENTEp su)
{
                    return su->blocco;
}

























