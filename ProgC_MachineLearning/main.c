#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// #include "main.h"
// #include "try_01.h"
#include "Perceptron.h"
#include "ArrayLib/ArrayLib.h"
#include "ArrayLib/Array2D.h"

// http://www.network-theory.co.uk/docs/gccintro/gccintro_11.html
// gcc -Wall main.c try_01.c -o TRY01
// gcc -Wall main.c ArrayLib/ArrayLib.h ArrayLib/Array2D.c -o arr_01
// gcc -Wall main.c Perceptron.c ArrayLib/ArrayLib.h ArrayLib/Array2D.c -o prc_01

// https://archive.ics.uci.edu/ml/index.php
// https://archive.ics.uci.edu/ml/machine-learning-databases/iris/

void func1 (void);
void func2 (void);

int main (int argc, char ** argv)
{
	printf("I'm a program and i wanna know. %d\n", MACRO_DI_PROVA);

	// func1();
	
	printf("-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-=-=-=-=-=-\n");

	func2();

	return 0;
}

void func1 (void)
{
	Array2D a1 = Array2D_Init(1, 2);
	sample smp, smps[6];

	Array2D_Print(a1);

	smp.d = 1;
	Array2D_Append(a1, smp);
	smp.d = 2;
	Array2D_Append(a1, smp);

	Array2D_Print(a1);

	smp.d = 3;
	Array2D_Append(a1, smp);
	smp.d = 4;
	Array2D_Append(a1, smp);

	smps[0] = Array2D_Index(a1, 0, 0);
	smps[1] = Array2D_Index(a1, 0, 1);
	smps[2] = Array2D_Index(a1, 1, 0);

	Array2D_Print(a1);

	smps[3] = Array2D_Index(a1, 1, 1);
	smps[4] = Array2D_Index(a1, 2, 0);
	smps[5] = Array2D_Index(a1, 2, 1);

	printf("%d, %d, %d, %d, ...\n", smps[0].d, smps[1].d, smps[2].d, smps[3].d);
	printf("%d, %d, ...\n", smps[4].d, smps[5].d);

	Array2D_Free(a1);
}

void func2 (void)
{
	Array2D X = Array2D_Init(100, 2);
	Array2D y = Array2D_Init(100, 1);
	sample smp;
	int counter = 0;

	FILE * irisdb = fopen("database_iris.txt", "r");
	char * line = NULL;
	char str[21] = "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0";
	size_t len = 0;
	ssize_t read;


	while ((read = getline(&line, &len, irisdb)) != -1) {
		// printf("%s", line);

		if (counter >= 100)
			break;
		counter++;

		int j = 0, c = 0;
		
		for (int i = 0; /*i < read*/; i++, j++) {

			// printf("|%d, %d| = %c \n", i, j, line[i]);

			if (line[i] == ',' && c < 4) {
				str[j] = '\0';

				if (c == 0 || c == 2) {
					sscanf(str, "%lf", &smp.lf);
					Array2D_Append(X, smp);
					// printf("%.2lf, ", smp.lf);
				}
				
				j = -1;
				c++;
				continue;
			}

			if ((line[i] == '\n' || line[i] == '\0') && c == 4) {
				str[j] = '\0';

				if (strncmp(str, "Iris-setosa", sizeof("Iris-setosa")) == 0 ) {
					smp.d = -1;
					Array2D_Append(y, smp);
				}
				if (strncmp(str, "Iris-versicolor", sizeof("Iris-versicolor")) == 0 ) {
					smp.d = 1;
					Array2D_Append(y, smp);
				}

				// printf("%s\n", str);
				break;
			}

			str[j] = line[i];
			//printf("%c", str[j]);
			//printf("%d", j);
		}
		// printf("\n");
	}

	fclose(irisdb);

	/*for (int i = 0; i < Array2D_Samples(X); i++) {

		printf("%d.  ", i);

		smp = Array2D_Get(X, i, 0);
		printf("%.2lf ", smp.lf);

		smp = Array2D_Get(X, i, 1);
		printf("%.2lf ", smp.lf);

		smp = Array2D_Get(y, i, 0);
		printf("%d\n", smp.d);
	}*/


	Perceptron_t p1 = Perceptron_Init(0.01f, 10);

	Perceptron_Fit(p1, X, y);

	Perceptron_Free(p1);

	Array2D_Free(X);
	Array2D_Free(y);
}