
#ifndef chat_server_segmento_h
#define chat_server_segmento_h




/* #################################################
   #*#*** Strc, enum                          ***#*#
   ################################################# */
typedef struct segmento  segmento;
#define SEGMENTO         segmento
#define SEGMENTOp        SEGMENTO *

typedef   char     __segmento_payload_t;

typedef   short       __segmento_part_t;
#define _S_1of1   1, 1

typedef   enum {                                        // SERVONO PER CAPIRE DA CHI È VENUTO IL MESSAGGIO
    //  0 ... 255  TOT
    
    // 0 ... 150  UTENTI
    ___SEGMENTO_HEAD_UTENTE1__      = 0,        // DA UTENTE, E DA QUALE
    ___SEGMENTO_HEAD_UTENTE150__    = 150,
    
    // 151 ... 199  usi futuri
    ___SEGMENTO_H_ERRORE_         = 160,
    
    // 200 ... 250  OPERAZIONI SISTEMA
    ___SEGMENTO_HEAD_IPMAC__      = 200,        // DA SISTEMA
    ___SEGMENTO_HEAD_NAME__       = 201,
    ___SEGMENTO_HEAD_IPADDR__     = 202,
    ___SEGMENTO_HEAD_MACADDR__    = 203,
    ___SEGMENTO_H_UTENTELIST__    ,
    
    ___SEGMENTO_H_YOUON_,
    ___SEGMENTO_H_CLOSE_
    
    
    // 251 ... 255  usi futuri
    
}                    __segmento_head_t;

#define _SEGMENTO_HEAD_LENGTH       (sizeof(__segmento_head_t))
#define _SEGMENTO_PART_LENGTH       (sizeof(__segmento_part_t))
#define _SEGMENTO_PAYLOAD_LENGTH    (sizeof(char)*514)
#define _SEGMENTO_LENGTH    ( (sizeof(__segmento_head_t))+(sizeof(__segmento_part_t))+(sizeof(char)*514)  )



/* #################################################
   #*#*** FUNZIONI                            ***#*#
   ################################################# */

SEGMENTOp   Segmento
        (__segmento_head_t head, __segmento_part_t npart, __segmento_part_t ofpart, __segmento_payload_t * payload);

void    Segmento_canc   (SEGMENTOp s);


void   segmento_setHead   (SEGMENTOp s, __segmento_head_t head);
void   segmento_setPayload   (SEGMENTOp s, __segmento_payload_t * payload);


__segmento_head_t    segmento_getHead    (SEGMENTOp s);
__segmento_payload_t *   segmento_getPayload    (SEGMENTOp s);


int    segmento_fromUtente  (SEGMENTOp s);


void    segmento_show   (SEGMENTOp s);





#endif
