
#ifndef chat_server_info_connessione_h
#define chat_server_info_connessione_h



/* #################################################
 #*#*** Librerie                            ***#*#
 ################################################# */
#include "segmento.h"


/* #################################################
   #*#*** Strc, enum                          ***#*#
   ################################################# */
typedef struct info_connessione  info_connessione;
#define INFO_CONNESSIONE         info_connessione
#define INFO_CONNESSIONEp        INFO_CONNESSIONE *

typedef     char *              __infconnss_interface_t;

typedef     int                 __infconnss_porta_t;

typedef     int                 __infconnss_sock_t;

typedef     struct sockaddr_in  __infconnss_ipsk_t;
typedef     int                 __infconnss_ipsk_family_t;
typedef     __int128_t          __infconnss_ipsk_addr_t;

typedef     char *              __infconnss_ip_t;

typedef     char *              __infconnss_mac_t;




/* #################################################
 #*#*** FUNZIONI                            ***#*#
 ################################################# */
#define infoConnessione         infConss

INFO_CONNESSIONEp   InfoConnessione
    (__infconnss_interface_t infc, __infconnss_porta_t porta, __infconnss_ipsk_family_t ip_family, __infconnss_ipsk_addr_t ip_addr);

void    InfoConnessione_canc   (INFO_CONNESSIONEp ic);


// FUNZIONE CHE RESTITUISCE IL MAC ADDRESS
// FUONZINE CHE RESTIRUISCE L'IP ADDRESS


int   infoConnessione_setSock     (INFO_CONNESSIONEp ic, __infconnss_sock_t sock);
int   infoConnessione_setIp      (INFO_CONNESSIONEp ic, __infconnss_ipsk_t ipstr);
int   infoConnessione_setIpAddr   (INFO_CONNESSIONEp ic, char * namehost);


__infconnss_sock_t     infoConnessione_getSock    (INFO_CONNESSIONEp ic);
__infconnss_ipsk_t *   infoConnessione_getIp      (INFO_CONNESSIONEp ic);
__infconnss_porta_t    infoConnessione_getPorta   (INFO_CONNESSIONEp ic);


// SERVER E CLIENT
int         infoConnessione_socket    (INFO_CONNESSIONEp ic, int pfinet, int sockstream, int ipprototcp);
int         infoConnessione_write     (INFO_CONNESSIONEp ic, SEGMENTOp s);
SEGMENTOp   infoConnessione_read      (INFO_CONNESSIONEp ic);
int         infoConnessione_close     (INFO_CONNESSIONEp ic);
// SERVER
int         infoConnessione_bind      (INFO_CONNESSIONEp ic);
int         infoConnessione_listen    (INFO_CONNESSIONEp ic, int codareq);
int         infoConnessione_accept    (INFO_CONNESSIONEp ic, INFO_CONNESSIONEp newic);
// CLIENT
int         infoConnessione_connect   (INFO_CONNESSIONEp ic, INFO_CONNESSIONEp serveric);



#endif















