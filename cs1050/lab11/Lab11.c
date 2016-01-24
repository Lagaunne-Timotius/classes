/*Timotius Andrean Patrick Lagaunne
  14173082
  TALYXD
  11/18/2013
  Lab code: //Comment the Code
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 50
//Structure definition//
typedef struct{
	int id;
	int grade;
} data;

data student[MAX];
//Function prototype//
int loadArray(char* filename);
void printArray(int size);
int searchArray(int size,int id,int ngrade);
int  writeContent(char* fname,int size);
void sortArray(int size);
int main(int argc,char** argv)
{
	//Error checking for the number of argument//
	if (argc !=3)
	{
		printf("Insufficent arguments");
		return -1;
	}
	//Error checking for existance of input//
	int size=loadArray(argv[1]);
	if(size==0)
        {
                printf("Unable to open the input file");
                return -1;
        }
	//Declaration of variables//
	int id, ngrade,search;
	//Display output//
	printf("Student Record\n");
	printArray(size);
	//Search ID and rewritng new grade//
	printf("\nEnter the ID of the student to search:");
	scanf("%d",&id);
	printf("Enter a grade of the student:");
	scanf("%d",&ngrade);
	// Checking for the existance of the id//
	if((search=searchArray(size,id,ngrade))==0)
	{
		printf("Student with id %d is not present in the class\n");
	}
	//Write a new file with the new revision//
	else
	{
		int x=writeContent(argv[2],size);
		//Print new output//
		printf("\nUpdated student record\n");
		printArray(size);
	}
	sortArray(size);
	//Bonus Part Sorting array//
	printf("\nBonus part\nPrinting sorted student record\n");
	printArray(size);

	return 0;	

}
int loadArray(char* filename)//Load the file and return the size of the array// 
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
	fclose(file);
	return size;
}
void printArray(int size)//Print the output//
{
	int counter;
	printf("%-6s%-6s\n","ID","Grade");
	for(counter=0;counter<size;counter++)
	{
		printf("%-6d%-6d\n",student[counter].id,student[counter].grade);
	}
	
}

int searchArray(int size,int id,int ngrade)//Search the id and rewrite the new grade//
{
	int counter;
	for(counter=0;counter<size;counter++)
	{
		if(student[counter].id==id)
		{
			student[counter].grade=ngrade;
			return 1;
		}
	}
	return 0;
}

int  writeContent(char* fname,int size)//Write a new file based on the revision of grade//
{
	int i=0;
        FILE* file=fopen(fname,"w");
	if(file==NULL)
	{
		return 0;
	}
	else
	{
        	
        	for(i=0;i<size;i++)
        	{
                	fprintf(file, "%3d %-3d \n" , student[i].id,student[i].grade);
        	}
        
	}
		
	fclose(file);
	return 1;

}
void sortArray(int size)//Sorting Array//
{
	int counter,counter2,counter3=0,keep1,keep2;
	for(counter=0;counter<size;counter++)
	{
		for(counter2=0;counter2<size-1;counter2++)
		{
			if(student[counter2].grade>student[counter2+1].grade)
			{
				keep1=student[counter2].id;
				keep2=student[counter2].grade;
				student[counter2].id=student[counter2+1].id;
				student[counter2].grade=student[counter2+1].grade;
				student[counter2+1].id=keep1;
                                student[counter2+1].grade=keep2;
				counter3++;
			}
		}
		if(counter3==0)
                break;
                counter3=0;

	}
}

