#include <stdio.h>
#include <string.h>
#include "calculator.h"

#define BUFFERSIZE 100

int main(int argc, char* argv[]) {
    
    
    char buffer[BUFFERSIZE];
	//Checking the error
    if (argc != 2) {
        printf("correct ussage: %s <input file>\n", argv[0]);
        return 1;
    }
	//Opening the file
    FILE* fp = fopen(argv[1], "r");
	//Checking the file
    if(fp == NULL) {
        printf("unable to open file: %s\n", argv[1]);
        return 1;
    }
	//Inputing the data inside the file
    while(fgets(buffer, BUFFERSIZE, fp)) {
        if (buffer[strlen(buffer)-1] == '\n') {
            buffer[strlen(buffer)-1] = '\0'; 
        }
        char *postfix = infix_to_postfix(buffer);
        int result = evaluate_postfix(postfix);
        printf("%s = %d\n", buffer, result);
    }
    
    return 0;
}
