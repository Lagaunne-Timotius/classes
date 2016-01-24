/*Timotius Andrean Patrick Lagaunne
  14173082
*/

#include <stdio.h>
#define max 100

int length(char *a);
int replace(char *s,int i);
int main(void)
{
	char p[max];
	int index,z;
	printf("Enter a string:");
	scanf("%s",p);
	printf("\nInput string is %s",p);
	printf("\nLength of the string is %d",length(p));
	printf("\nEnter an index location:");
	scanf("%d",&index);
	z=replace(p,index);
	if(z==0)
	{	 
		printf("\nInvalid index");
	}
	else
	{
		printf("\nString after replacement operation is %s \n",p);
	}
}
int length(char *aPtr)
{	
	int counter=0;
	while(*aPtr!='\0')
	{
		counter++;
		aPtr++;
	}
	return counter;
}

int replace(char *s,int i )
{
	int counter;
	if (i<0||i>(length(s)-1))
	{
		return 0;
	}
	else
	{
		*(s+i)='#';
		return 1;
	}
}

		





