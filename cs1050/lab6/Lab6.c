/*Timotius Andrean Patrick Lagaunne
  TALYXD
  Lab Code:10/7/2013
  14173082
*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX 100
#define MAX2 10
//function prototype//
int check_error(int);
void initialize_array(int[],int);
void print_array(int[],int);
int count_numbers(int[],int,int);
void frequency(int[],int[],int);
int mode(int[]);
void print_histogram(int[]);
void sort_array(int[],int);
int main(void)
{
	srand(time(NULL));
	int SIZE,counter; 
	int a[MAX];
	int b[MAX2]={0};
	printf("Input the size of the first input:");
	scanf("%d",&SIZE);
	while (check_error(SIZE)==0)
	{
		printf("Invalid input enter the size of the input again");
		scanf("%d",&SIZE);
	}
	initialize_array(a,SIZE);
	printf("Input array\n");
	print_array(a,SIZE);
	frequency(a,b,SIZE);
	printf("\nMode for the array is number %d",mode(b));
	printf("\nPrinting histogram\n");
	print_histogram(b);
	printf("Bonus part\n");
	printf("\nArray before sorting\n");
	print_array(a,SIZE);	
	printf("\nArray after sorting\n");
	sort_array(a,SIZE);
	print_array(a,SIZE);
	printf("\n");
}
int check_error(int b)
{	
	if(b<0||b>100)
	return 0;	
	else 
	return 1;
}
void initialize_array(int a[],int b)
{
	int counter;
        for(counter=0;counter<b;counter++)
	{
		a[counter]=rand()%10;	
	}
}
void print_array(int a[],int b)
{
	int counter;
        for(counter=0;counter<b;counter++)
        {
		printf("%d ",a[counter]);
        }

}
int count_numbers(int a[],int b,int c)
{
	int counter,counter2;
	for(counter=0;counter<b;counter++)
        {
                if (a[counter]==c)
		counter2++;
        }
	return counter2;
}
void frequency(int a[],int b[],int c)
{
	int counter;
	for(counter=0;counter<c;counter++)
	{
			b[counter]=count_numbers(a,c,counter);
	}
}
int mode(int b[])
{
	int counter,max;
	max=0;
	for (counter=1;counter<10;counter++)
	{
		if (b[max]<b[counter])
		max=counter;
	}
	return max;
}

void print_histogram(int b[])
{
	int counter,counter2;
	for(counter=0;counter<10;counter++)
	{
		printf("%d:",counter);
		for(counter2=0;counter2<b[counter];counter2++)
		{
			printf("*");
		}
		printf("\n");
	}
}
void sort_array(int a[],int b)
{
	int counter,counter2;
	for(counter=0;counter<b;counter++)
	{
		for(counter2=0;counter2<b;counter2++)
		{
			if (a[counter]>a[counter2])
			a[counter]=a[counter2];
		}
	}
}
