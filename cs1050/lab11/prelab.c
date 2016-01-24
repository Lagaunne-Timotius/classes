/*Timotius Andrean Patrick Lagaunne
  14173082
  TALYXD
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 50

struct data{
	int id;
	int grade;
}student[MAX];

int loadArray(char* filename);
void printArray(int size);
int main(int argc,char** argv)
{
	if (argc !=2)
	{
		printf("Insufficent arguments");
		return -1;
	}
	if(strcmp(argv[1],"input.txt")!=0)
	{
		printf("Unable to open the input file");
		return -1;
	}
	int size=loadArray(argv[1]);
	printArray(size);
	

	
	return 0;	

}
int loadArray(char* filename)
{
	int i=0;
	int id;
	int grade;
	FILE* file=fopen(filename,"r");
	if(file==NULL)
	{
		return 0;
	}
	
	int size;
	
	fscanf(file, "%d" , &size);
	for(i=0;i<size;i++)
	{
		fscanf(file, "%d%d" , &id,&grade);
		student[i].id=id;
		student[i].grade=grade;
	}
	student[size].id='\0';
	student[size].grade='\0';

	fclose(file);
	return size;
}
void printArray(int size)
{
	int counter;
	printf("%-6s%-6s\n","ID","Grade");
	for(counter=0;counter<size;counter++)
	{
		printf("%-6d%-6d\n",student[counter].id,student[counter].grade);
	}
	
}

