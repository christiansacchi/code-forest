
/* #################################################
   #*#*** Librerie                            ***#*#
   ################################################# */
#include "chat_general_header.h"

#include "info_connessione.h"
#include "segmento.h"


/* #################################################
   #*#*** Macro                               ***#*#
   ################################################# */
#define MACADDR_LENGTH     6
#define IPADDR_LENGTH      4
#define INTERFACE_LENGTH   5


/* #################################################
   #*#*** Strc, enum                          ***#*#
   ################################################# */
struct info_connessione {
        __infconnss_interface_t interface;      // char *
        __infconnss_porta_t     porta;          // int
        __infconnss_sock_t      sock;           // int
        __infconnss_ipsk_t      ipstr;          // struct sockaddr_in   // IP per la gestione del sock
    
        // NON SI È ANCORA TROVATO UN MODO PER PRENDERLI
        __infconnss_ip_t        ipaddr;         // char *               // Stringa che continene IP standard
        __infconnss_mac_t       macaddr;        // char *
};




/* #################################################
   #*#*** FUNZIONI                            ***#*#
   ################################################# */

// InfoConnessione("en1", SERVER_PORT, AF_INET, INADDR_ANY);
INFO_CONNESSIONEp   InfoConnessione
        (__infconnss_interface_t infc, __infconnss_porta_t porta, __infconnss_ipsk_family_t ip_family, __infconnss_ipsk_addr_t ip_addr)
{
    INFO_CONNESSIONEp ic = calloc(1, sizeof(INFO_CONNESSIONE));
    
    
    ic->interface = calloc(INTERFACE_LENGTH, sizeof(char));
    if (infc != NULL)
        strncpy(ic->interface, infc, INTERFACE_LENGTH);
    
    ic->porta = porta;
    
    ic->sock = -1;
    
    memset(&ic->ipstr, 0, sizeof(ic->ipstr));
    ic->ipstr.sin_family = ip_family;
    ic->ipstr.sin_addr.s_addr = htonl(ip_addr);
    ic->ipstr.sin_port = htons(porta);
    
    // ic->macaddr = calloc(MACADDR_LENGTH, sizeof(char));     // Inizializzati ma non utilizzati
    // ic->ipaddr = calloc(IPADDR_LENGTH, sizeof(char));       // per MAC e IP
    ic->macaddr = NULL;
    ic->ipaddr = NULL;
    
    return ic;
}

void    InfoConnessione_canc   (INFO_CONNESSIONEp ic)
{
    free(ic->interface); ic->interface = NULL;
    // free(ic->ipaddr);  free(ic->macaddr);  // Inizializzati a NULL
    free(ic);     ic = NULL;
}


// FUNZIONE CHE RESTITUISCE IL MAC ADDRESS
// FUONZINE CHE RESTIRUISCE L'IP ADDRESS



int   infoConnessione_setSock   (INFO_CONNESSIONEp ic, __infconnss_sock_t sock)
{
                return ic->sock = sock;
}

int   infoConnessione_setIp   (INFO_CONNESSIONEp ic, __infconnss_ipsk_t ipstr)
{
                ic->ipstr = ipstr;
                return 0;
}
int   infoConnessione_setIpAddr   (INFO_CONNESSIONEp ic, char * namehost)
{
                struct hostent * h = gethostbyname(namehost);
                memcpy(&ic->ipstr.sin_addr.s_addr, h->h_addr, sizeof(h->h_length));
                return 0;
}


__infconnss_sock_t    infoConnessione_getSock    (INFO_CONNESSIONEp ic)
{
                return ic->sock;
}
__infconnss_ipsk_t  *  infoConnessione_getIp      (INFO_CONNESSIONEp ic)
{
                return &ic->ipstr;
}
__infconnss_porta_t    infoConnessione_getPorta   (INFO_CONNESSIONEp ic)
{
    return ic->porta;
}


// Server e client --- SOCKET, WRITE, READ
int   infoConnessione_socket    (INFO_CONNESSIONEp ic, int pfinet, int sockstream, int ipprototcp)
{
                (ic->sock = (int)socket(pfinet, sockstream, ipprototcp));
    
                int on = 1;
                setsockopt(  ic->sock, SOL_SOCKET, SO_REUSEADDR, (char *)&on, sizeof(on)  );
    
                return ic->sock;
}
int         infoConnessione_write    (INFO_CONNESSIONEp ic, SEGMENTOp s)    // verso tutti client per server, verso server per client
{
                if (    send(ic->sock, s, _SEGMENTO_LENGTH, 0)/*write(ic->sock, s, _SEGMENTO_LENGTH)*/  <= 0 )
                    return -1;
    
                return 0;
}
SEGMENTOp   infoConnessione_read     (INFO_CONNESSIONEp ic)   // da ANYCAST per server, da server per client
{
                SEGMENTOp s = NULL; s = Segmento(0, 0, 0, 0);
                if (    recv(ic->sock, s, _SEGMENTO_LENGTH, 0)/*read(ic->sock, s, _SEGMENTO_LENGTH)*/  <= 0 )
                    return NULL;
    
                return s;
}
int         infoConnessione_close     (INFO_CONNESSIONEp ic)
{
                return shutdown(ic->sock, SHUT_RDWR);
}


// Server --- BIND, LISTEN, ACCEPT
int   infoConnessione_bind      (INFO_CONNESSIONEp ic)
{
                return   bind( (int)ic->sock, (struct sockaddr *)&ic->ipstr , sizeof(ic->ipstr) );
}

int   infoConnessione_listen    (INFO_CONNESSIONEp ic, int codareq)
{
                return   listen(  (int)ic->sock, codareq  );
}

int   infoConnessione_accept    (INFO_CONNESSIONEp ic, INFO_CONNESSIONEp newic)
{
                socklen_t size_ip = sizeof(newic->ipstr);
                return  newic->sock = accept(  ic->sock, (struct sockaddr *)&newic->ipstr, &size_ip  );
    // Dovrà essere messo qui un if dentro al quale, se la accept va a buon fine, si dovrà inviare \
       un messaggio per consegnare ip e mac
}


// Client --- CONNECT
int   infoConnessione_connect    (INFO_CONNESSIONEp ic, INFO_CONNESSIONEp serveric)
{
                return connect(  ic->sock, (struct sockaddr *)&serveric->ipstr, sizeof(serveric->ipstr)  );
    // Dovrà essere messo qui un if dentro al quale, se la accept va a buon fine, si dovrà inviare \
    un messaggio per consegnare ip e mac
}












