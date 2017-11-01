
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#define max_len_name 8
#define pause system("pause");

int read_line(char str[], int n) {
    int ch, i = 0;
    
    while (isspace(ch = getchar()))
        ;
    while (ch != '\n' && ch != EOF) {
        if (i < n)
            str[i++] = ch;
        ch = getchar();
    }
    str[i] = '\0';
    return i;
}

int main(int argc, const char * argv[])
{
    pause;
    
    char str[max_len_name+1];
    char command[6+max_len_name+4+1];
    
    if (argc > 1)
        strcpy(str, argv[1]);
    else {
        printf("Input nome programma: ");
        read_line(str, max_len_name+1);
    }
    
    /* TASM */
    strcpy(command, "tasm ");
    strcat(command, str);
    strcat(command, ".asm");
    system(command);
    pause;
    
    /* TLINK */
    strcpy(command, "tlink ");
    strcat(command, str);
    strcat(command, ".obj");
    system(command);
    pause;
    
    /* TD or LAUNCH */
    printf("TD [0] or LAUNCH [tasto a caso]: ");
    while (getchar() == '\n');
    if (getchar() == '0') {
        strcpy(command, "td ");
        strcat(command, str);
        strcat(command, ".exe");
        system(command);
    } else
        system(command);
    
    pause;
    return 0;
}

