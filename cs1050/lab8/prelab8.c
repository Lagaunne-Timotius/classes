/*Timotius Andrean Patrick Lagaunne
  14173082
  10/20/2013

*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX 100

int length(char a[]);
int replace(char[],char);
int main(void)
{
	char x[MAX]={0};
	char c;
	int counter;
	printf("Enter a string:");
	scanf("%s",x);
	printf("\nInput string is %s",x);
	int len=length(x);
	for(counter=0;counter<MAX;counter++)
	{
		printf("x[counter] =%c\n",x[counter]);
	}
	printf("\n Length of the string is %d",len);
	printf("\n Enter the character to replace:");
	scanf("%c",&c);
	int z=replace(x,c);
	if (z=0)
	printf("\nCharacter %c is not presented in the string",c);
	counter=0;
	if (z=1)
	{
		printf("\nString after the replacement is %s",x);
	}




}
int length(char a[])
{
	int count=0,counter;
	while (a[counter]!='\0')
	{
		 counter++;
	}
	return counter;
}


	
int replace(char a[],char b)
{
	int counter,count=0;
	for(counter=0;counter<=length(a);counter++)
	{
		if (a[counter]==b)
		{
			a[counter]='#';
			count++;
		}
	}
	if (count!=0)
	return 1;
	else
	return 0;
}
	

