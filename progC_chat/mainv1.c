
#include "chat.h"
#include "segmento.h"
#include "chat_general_header.h"


#define SERVER_PORT 12345
#define BUF_SIZE 4096
#define QUEUE_SIZE 10



void * scrittore1 (void * argv);
void * lettore1 (void * argv);

int   main2 (int argc, const char * argv[])
{
    
    INFO_CONNESSIONEp ic;
    //SEGMENTOp s = NULL;
    char str[_SEGMENTO_PAYLOAD_LENGTH];      // prima usata per nome, poi per str
    
    
    ic = InfoConnessione("en1", SERVER_PORT, AF_INET, -1);
    gethostname(str, 128);
    infoConnessione_setIpAddr(ic, str);
    
    if ( infoConnessione_socket(ic, PF_INET, SOCK_STREAM, IPPROTO_TCP) < 0) perror("SOCKET");
    if ( infoConnessione_connect(ic, ic) < 0)                               perror("CONNECT");
    
    
    
    
    int pid, pid2;
    pthread_t t, t2;
    
    // Inizializzazione thread
    pid = pthread_create(&t, NULL, scrittore1, ic);
    pid2 = pthread_create(&t2, NULL, lettore1, ic);
    
    // Avvio thread
    pthread_join(t, NULL);
    pthread_join(t2, NULL);
    
    
    return 0;
}



void * scrittore1 (void * ic)
{
    char str[_SEGMENTO_PAYLOAD_LENGTH];
    SEGMENTOp s = NULL;
    
    loop {
        printf("> "); read_line(str, sizeof(str));
        s = Segmento(1, _S_1of1, str);
        infoConnessione_write(ic, s);
        Segmento_canc(s); s = NULL;
    }
    
    return NULL;
}

void * lettore1 (void * ic)
{
    SEGMENTOp s = NULL;
    
    loop {
        
        if ( (s = infoConnessione_read(ic)) == NULL ) {
            perror("s == null");
            continue;
        }
        
        segmento_show(s);
        Segmento_canc(s);
    }
    
    return NULL;
}
