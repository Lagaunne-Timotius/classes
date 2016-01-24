/*Timotius Andrean Patrick Lagaunne
  14173082
  TALYXD
  lab code :Nov 11 2013
*/

#include <stdio.h>
#include<string.h>
#include <ctype.h>
void readInput(char*);
void cleanString(char*,char*);
int dnaSequence(char*,char[][5]);
void printDNAseq(char[][5],int n);
int checkDNAseq(char*s);
int main(void)
{
	int n;
	char input[80];
	char clean[80];
	char dna[25][5];
	int counter;
	puts("Enter the input string:");
	readInput(input);	
	printf("\nInput string is ");
	printf("%s",input);
	printf("\nCleaned string is ");
	cleanString(input,clean); 
	printf("%s",clean);
	n=dnaSequence(clean,dna);
	printDNAseq(dna,n);
	for(counter=0;counter<n;counter++)
	{
		if(checkDNAseq(*(dna+counter))==1)
		{
			printf("Sequence %s is a human DNA",*(dna+counter));
		}
		if(checkDNAseq(*(dna+counter))==2)
                {
                        printf("Sequence %s is a cow DNA",*(dna+counter));
                }
		if(checkDNAseq(*(dna+counter))==3)
                {
                        printf("Sequence %s is a horse DNA",*(dna+counter));
                }
		if(checkDNAseq(*(dna+counter))==4)
                {
                        printf("Sequence %s is not a DNA sequence",*(dna+counter));
                }
		printf("\n");
	}
	
}

void readInput(char*pointer)
{
 	char ch;
	int i;
	i=0;
	while((ch=getchar())!='\n')
	{
		*(pointer+i)=ch;
		i++;

	}
        *(pointer+i)='\0';

}
	


void cleanString(char*pointer,char* pointer2)
{
	int counter2=0,counter3=0,counter=0;
	while(*(pointer+counter3)!='\0')
	{
		if(isalpha(*(pointer+counter3)))
		{
			*(pointer2+counter2)=*(pointer+counter3);
			*(pointer2+counter2)=toupper(*(pointer2+counter2));
			counter2++;
		}
	counter3++;
	}
	*(pointer2+counter3)='\0';

}
int dnaSequence(char*clean,char dna[][5])
{	int counter,counter2,counter3=0;
	int row=strlen(clean)/4;
	for(counter=0;counter<row;counter++)
	{
		for(counter2=0;counter2<4;counter2++)
		{
			dna[counter][counter2]=*(clean+counter3);
			counter3++;
		}
	dna[counter][counter2]='\0';
	}
	return row;
}
	
void printDNAseq(char dna[][5],int n)
{
	int counter,counter2;
	printf("\nDNA sequences are\n");
	for(counter=0;counter<n;counter++)
	{
		for(counter2=0;counter2<4;counter2++)
		{
			printf("%c",dna[counter][counter2]);
		}
		printf("\n");
	}
}
int checkDNAseq(char*dna)
{
	if(strcmp(dna,"ACTG")==0)
	return 1;
	if(strcmp(dna,"ACTC")==0)
        return 2;
	if(strcmp(dna,"ACTH")==0)
        return 3; 
	else
        return 4;
}









