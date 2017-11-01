#include "chat.h"
#include "segmento.h"
#include "chat_general_header.h"


#define SERVER_PORT 12345
#define BUF_SIZE 4096
#define QUEUE_SIZE 10



int   main (int argc, const char * argv[])
{
    char str[20];
    char hostname[128];
    
    gethostname(hostname, 128);
    
    printf("\n> "); read_line(str, 20);
    CHAT_UTENTEp c = chat_accedi(str, hostname, SERVER_PORT);
    /*printf("\n> "); read_line(str, 20);
    c = chat_accedi(str, hostname, SERVER_PORT);
    printf("\n> "); read_line(str, 20);
    c = chat_accedi(str, hostname, SERVER_PORT);*/
    
    
    printf("ho finito.\n");
    
    
    int pid, pid2;
    pthread_t t, t2;
    
    // Inizializzazione thread
    pid = pthread_create(&t, NULL, scrittore, c ); // GET_INFO_FROM_LIST_OF(0)
    pid2 = pthread_create(&t2, NULL, lettore, c ); // GET_INFO_FROM_LIST_OF(0)
    
    // Avvio thread
    pthread_join(t, NULL);
    pthread_join(t2, NULL);
    
    
    return 0;
}
// FFFFFFFFFFFFFFFFFFFFF








