
#ifndef chat_server_stato_utente_h
#define chat_server_stato_utente_h




/* #################################################
   #*#*** Strc, enum                          ***#*#
   ################################################# */
typedef struct stato_utente  stato_utente;
#define STATO_UTENTE         stato_utente
#define STATO_UTENTEp        STATO_UTENTE *

typedef enum {
            ___STATUTENTE_GRADO_MOC__       = 0,
            ___STATUTENTE_GRADO_ADMIN__     ,
            ___STATUTENTE_GRADO_UTENTE__
}   __statutente_grado_t;
typedef enum {
            ___STATUTENTE_STATO_ON__        = 3,
            ___STATUTENTE_STATO_AFK__       ,
            ___STATUTENTE_STATO_OCCUPATO__
}   __statutente_stato_t;
typedef enum {
            ___STATUTENTE_BLOCCO_NONE__     = 6,
            ___STATUTENTE_BLOCCO_MUTE__     ,
            ___STATUTENTE_BLOCCO_BAN__
}   __statutente_blocco_t;

#define _SU__MOC_ON_NONE    ___STATUTENTE_GRADO_MOC__,___STATUTENTE_STATO_ON__,___STATUTENTE_BLOCCO_NONE__
#define _SU__UTENTE_ON_NONE    ___STATUTENTE_GRADO_UTENTE__,___STATUTENTE_STATO_ON__,___STATUTENTE_BLOCCO_NONE__



/* #################################################
   #*#*** FUNZIONI                            ***#*#
   ################################################# */
STATO_UTENTEp   StatoUtente        (__statutente_grado_t grado, __statutente_stato_t stato, __statutente_blocco_t blocco);
STATO_UTENTEp   StatoUtente_grado  (__statutente_grado_t grado);

void            StatoUtente_canc   (STATO_UTENTEp su);


void   statoUtente_setGrado   (STATO_UTENTEp su, __statutente_grado_t grado);
void   statoUtente_setStato   (STATO_UTENTEp su, __statutente_stato_t stato);
void   statoUtente_setBlocco  (STATO_UTENTEp su, __statutente_blocco_t blocco);

__statutente_grado_t    statoUtente_getGrado    (STATO_UTENTEp su);
__statutente_stato_t    statoUtente_getStato    (STATO_UTENTEp su);
__statutente_blocco_t   statoUtente_getBlocco   (STATO_UTENTEp su);





#endif
