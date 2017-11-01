#ifndef chat_server_chat_general_header_h
#define chat_server_chat_general_header_h



/* #################################################
   #*#*** Librerie                            ***#*#
   ################################################# */
// Standard
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <errno.h>
#include <stdbool.h>
#include <fcntl.h>
// Gestione thread
#include <pthread.h>
#include <semaphore.h>
// Gestione socket
#include <arpa/inet.h>
#include <sys/fcntl.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <netinet/in.h>
#include <sys/types.h>
// Programma
#include "chat.h"
#include "utente.h"
#include "info_connessione.h"
#include "stato_utente.h"
#include "segmento.h"


/* #################################################
   #*#*** Macro                               ***#*#
   ################################################# */
#define loop    while(1)
#define LOOP    loop


/* #################################################
 #*#*** Strc, enum                          ***#*#
 ################################################# */


/* #################################################
 #*#*** FUNZIONI                            ***#*#
 ################################################# */

int     read_line    (char str[], int n);




#endif
