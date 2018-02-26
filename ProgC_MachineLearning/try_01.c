
#include "try_01.h"

#include <stdio.h>
#include <stdlib.h>


struct try01
{
	int a;
	float b;
	bool h;
};


Try01 Try01_init (void) {
	
	Try01 self = malloc(sizeof(struct try01));

	return self;
}