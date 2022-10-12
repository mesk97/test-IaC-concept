#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main (int argc, char ** argv)
{
	int v = 3;
	printf("Code  is at %p \n", (void *)main);
	printf("Heap  is at %p \n", malloc(8));
	printf("Stack is at %p \n", (void *)&v);

	sleep (100);
	return 0;
}
