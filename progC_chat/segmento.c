
/* #################################################
   #*#*** Librerie                            ***#*#
   ################################################# */
#include "chat_general_header.h"

#include "segmento.h"



/* #################################################
   #*#*** Macro                               ***#*#
   ################################################# */
#define HEAD_LENGTH       _SEGMENTO_HEAD_LENGTH
#define PART_LENGTH       _SEGMENTO_PART_LENGTH
#define PAYLOAD_LENGTH    _SEGMENTO_PAYLOAD_LENGTH
#define SEGMENTO_LENGTH   _SEGMENTO_LENGTH



/* #################################################
   #*#*** Strc, enum                          ***#*#
   ################################################# */
struct segmento {
        __segmento_head_t       head;
        __segmento_part_t       npart;      // --> npart / ofpart
        __segmento_part_t       ofpart;     // --> 1/2, 2/2 [messaggio composto da due parti]
        __segmento_payload_t    payload;
};
// __segmento_part_t
// il messaggio appena arriva a un peer viene controllato per vedere se è diviso in parti
// controllando ofpart che sia maggiore di uno. se lo è aspetta fin quando non gli arrivano i pezzi dell'intero messaggio.
// poi può spedire il messaggio ancora una volta diviso.
// bisogna aspettare che tutti i pezzi arrivino perchè potrebbeno arrivano non uno di fila all'alto e perchè
// il messaggio richiede di essere stampato. se il messaggio arrivo a un utente allora questo non lo rinvierà indietro

// la lista dei messaggi da completare avrà un posto per ogni utente così quando arriva il messaggio il programma
// dovrà andarea vedere se nella lista dei messaggi da completare alla posizione indiacata da head c'è qualcosa


/* #################################################
   #*#*** FUNZIONI                            ***#*#
   ################################################# */

SEGMENTOp   Segmento
        (__segmento_head_t head, __segmento_part_t npart, __segmento_part_t ofpart, __segmento_payload_t * payload)
{
                SEGMENTOp s = NULL;
                s = calloc(1, _SEGMENTO_LENGTH);
                memset(s, 0, _SEGMENTO_LENGTH);
    
                s->head = head;
    
                s->npart = npart; s->ofpart = ofpart;
                
                // s->payload = calloc(PAYLOAD_LENGTH, sizeof(char));
                memset(&s->payload, 0, PAYLOAD_LENGTH);
                if (payload != NULL) strncpy(&s->payload, payload, PAYLOAD_LENGTH);
    
                return s;
}

void    Segmento_canc   (SEGMENTOp s)
{
                //free(s->payload);   s->payload = NULL;                free(s);    s = NULL;
}


void   segmento_setHead   (SEGMENTOp s, __segmento_head_t head)
{
                s->head = head;
}
void   segmento_setPayload   (SEGMENTOp s, __segmento_payload_t * payload)
{
                strncpy(&s->payload, payload, PAYLOAD_LENGTH);
}


__segmento_head_t    segmento_getHead    (SEGMENTOp s)
{
                return s->head;
}
__segmento_payload_t *   segmento_getPayload    (SEGMENTOp s)
{
                return &s->payload;
}


int    segmento_fromUtente  (SEGMENTOp s)
{
    if (   (s->head >= ___SEGMENTO_HEAD_UTENTE1__)  &&  (s->head <= ___SEGMENTO_HEAD_UTENTE150__) )
        return 0;   // Il messaggio è di un utente
    return -1;      // Il messaggio non è di un utente
}



void    segmento_show   (SEGMENTOp s)
{
    printf(">> %d, %d/%d >", s->head, s->npart, s->ofpart);
    printf("  %s\n", &s->payload);
    
    /*printf("SEGMENTO --\n");
    printf("  head: %3d, parte: %d/%d\n", s->head, s->npart, s->ofpart);
    printf("  %s", &s->payload);
    printf("\n--\n");*/
}













