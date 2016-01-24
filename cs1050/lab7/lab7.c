/*Timotius Andrean Patrick Lagaunne
  14173082
  TALYXD
  10/14/2013
  LAB CODE: MON142013
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define COL_SIZE 100
//function prototype//
int check_error(int num);//Checking size of array//
void initialize_2Darray(float x[][COL_SIZE],int size);//Initialize array value//
void print_2Darray(float x[][COL_SIZE],int size);//Print array//
float column_average(float scores[][COL_SIZE],int size,int columnToAverage);//average per column//
void average_scores(float scores[][COL_SIZE],int size);//print average score//
char compute_grade(float scores[][COL_SIZE],int size,int student);//Compute overall grade//
float search_max(float x[][COL_SIZE],int row,int col,int size);//finding max in specific row or column//
int main(void)
{
	//variable declaration//
	int size,student,row,col;
	float scores[COL_SIZE][COL_SIZE];
	srand(time(NULL));
	//size of array input//
	printf("Enter the size of the array:");
	scanf("%d",&size);
	//error checking//
	while(check_error(size)==0)
	{
		printf("Invalid input enter the size of the array again:");
		scanf("%d",&size);
	}
	//print array//
	printf("\nScores:\n");
	initialize_2Darray(scores,size);
	print_2Darray(scores,size);
	printf("\n");
	//average score// 
	average_scores(scores,size);
	//student number input//
	printf("Enter student number (1-%d):",size);
	scanf("%d",&student);
	//Overal grade for specific student// 
	printf("\nOverall grade for %dth student is %c",student,compute_grade(scores,size,student));
	//input row//
	printf("\nEnter the row (1-%d):",size);
        scanf("%d",&row);
	//input column//
	printf("Enter the col (1-%d):",size);
        scanf("%d",&col);
	//the largest number present in specific row and column//
	printf("The largest number present in row %d or col %d is %.2f\n",row,col,search_max(scores,row,col,size));
	printf("Bonus part");
	printf("\nArray before sorting\n");
	print_2Darray(scores,size);	

}	
int check_error(int num)
{
	if(num<=0||num>100)
	return 0;
	else
	return 1;
}
void initialize_2Darray(float x[][COL_SIZE],int size)
{
	int countera,counterb;
	for(countera=0;countera<size;countera++)
	{
		for(counterb=0;counterb<size;counterb++)
		{
			x[countera][counterb]=100*((float)rand()/RAND_MAX);
		}
	}
}

void print_2Darray(float x[][COL_SIZE],int size)
{
	int countera,counterb,column,row;
	column=1;
	printf("   ");
	for(countera=0;countera<size;countera++)
        {
                printf("   C%d   ",column);
		column++;
        }
	row=1;
	printf("\n");
	for (countera=0;countera<size;countera++)
	{	
		printf("S%d:",row);
		row++;
		for(counterb=0;counterb<size;counterb++)
		{	
			printf(" %3.2f  ",x[countera][counterb]);
		}
		printf("\n");
	}
}
		
	
float column_average(float scores[][COL_SIZE],int size,int columnToAverage)
{
	int countera,counterb,sum=0;
	float average;
	for(countera=0;countera<size;countera++)
	{
		sum=sum+scores[countera][columnToAverage];
	}

	average=(float)sum/size;
	return average;
}
void average_scores(float scores[][COL_SIZE],int size)
{
	int countera;
	for(countera=0;countera<size;countera++)
	{
		printf("Course %d average score is %.2f\n",countera+1,column_average(scores,size,countera));
	}
}
	
char compute_grade(float scores[][COL_SIZE],int size,int student)
{
	int countera,counterb,sum=0;
	float average;
	for(countera=0;countera<size;countera++)
	{
		sum=sum+scores[student-1][countera];
	}
	average=(float)sum/size;
	if(average<60)
	return 'F';
	if(average>=60 && average<70)
	return 'D';
	if(average>=70 && average<80)
        return 'C';
 	if(average>=80 && average<90)
        return 'B';
	else
	return 'A';
}
float search_max(float x[][COL_SIZE],int row,int col,int size)
{
	int countera;
	float max;
	max=0;
	for(countera=0;countera<size;countera++)
	{
			if (max<x[countera][col-1])
			max=x[countera][col-1];
			if (max<x[row-1][countera])
			max=x[row-1][countera];
	}
	return max;
}


