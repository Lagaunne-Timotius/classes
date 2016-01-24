/*Timotius Andrean Patrick Lagaunne
  14173082
  10/20/2013
  LAB CODE: 23040046
*/

#include<stdio.h>
#define MAX 100
//Prototype function//
int length(char a[]);
void reverse(char a[],char b[]);
void sort(char a[]);
int search(char a[],char c);
void merge(char a[],char b[], char c[]);
int main(void)
{
	//Variable declaration//
	char a[MAX];
	char b[MAX];
	char d[MAX];
	char c;
	int counter;
	//input//
	printf("Enter a string:");
	scanf("%s",a);
	//Dsplay string//
	printf("\nInput string is %s",a);
	//apply function protoype//
	reverse(a,b);
	sort(a);
	//Display reverse string//
	printf("\nReverse string is %s",b);
	//Display Sorted String//
	printf("\nSorted string is %s",a);
	scanf("%c",&c);	
	//Input character want to be search//
	printf("\nEnter a character to search:");
	scanf("%c",&c);
	//Display output//
	if (search(a,c)==0)
	printf("\nCharacter %c is not presented in the string\n",c);
	if (search(a,c)!=0)
	printf("\nCharacter %c is presented %d times in the string",c,search(a,c));
	//Bonus Part//
	printf("\nBonus part");
	//New String input//
	printf("\nEnter a new string:");
        scanf("%s",b);
	//Display output//
	printf("First string is %s",a);
	printf("\nSecond string is %s",b);
	merge(a,b,d);
	printf("\nMerged string is %s\n",d);
	

}
int length(char a[])//Counting length of the string//
{
	int count,counter=0;
	while (a[counter]!='\0')
	{
		 counter++;
	}
	return counter;
}
void reverse(char a[],char b[])//Reversing the first array//
{
	int counter;
	for(counter=0;counter<length(a);counter++)
	{
		b[counter]=a[(length(a)-(counter+1))];
	}
	
}
void sort(char a[])//Sorting the array//
{
	int counter,counter2;
	char hold;
	for(counter2=1;counter2<length(a);counter2++)
	{
		for(counter=0;counter<length(a)-1;counter++)
		{
			if(a[counter]>a[counter+1])
			{
				hold=a[counter];
				a[counter]=a[counter+1];
				a[counter+1]=hold;
			}
		}		
	}	
		
}
int search(char a[],char b)//Search and count a character//
{
	int counter,count=0;
	for(counter=0;counter<length(a);counter++)
	{
		if (a[counter]==b)
		{
			count++;
		}
	}
	return count;
}
	
void merge (char a[],char b[],char c[])//Merge 2 arrays//
{
	int counter,constant,counter2,compare,count,max;
	if (length(a)<length(b))
	{
		compare=length(a);
		max=length(b);
	}
	else
	{
		compare=length(b);
		max=length(a);
	}
	counter=0;
	c[counter]=a[counter];
	for(counter=1;counter<=compare;counter++)
	{
		c[2*counter-1]=b[counter-1];
		c[(2*counter)]=a[counter];
		
	}
	c[2*counter-1]=b[counter];
	constant=counter;
	if (length(a)<length(b))
	{
		for(counter2=0;counter2<(max-compare)+1;counter2++)
		{
			counter++;
			c[2*constant+counter2]=b[counter];
		}
	}	
	else
	{
		for(counter2=0;counter2<(max-compare);counter2++)
                {
           		counter++;
			c[2*constant+counter2]=a[counter];
	
                }

	}

}	
