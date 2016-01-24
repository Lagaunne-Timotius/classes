/*Timotius Andrean Patrick Lagaunne
  14173082
  10/28/2013
  labcode:Oct28
*/

#include <stdio.h>
#define max 100

//Function Prototypes//
int length(char *a);
int replace(char *s,int i);
void copy(char*,char*);
void concatenate(char*,char*,char*);
int prefix(char*,char*);
int substring(char*,char*);
int main(void)
{	//Declaration of Variables//
	char p[max];
	char x[max];
	char f[max];
	char s[max];
	char d[max];
	char e[max];
	char b[max];
	char c[max];
	int index,z;
	char *pPtr=p;
	char *xPtr=x;
	char *sPtr=s;
	char *fPtr=f;
	char *dPtr=d;
	char *ePtr=e;
	char *cPtr=c;
	char *bPtr=b;
	//Input first String//
	printf("Enter first string:");
	scanf("%s",p);
	//Display of first String//
	printf("\nFirst string is %s",p);
	//Copy of First String//
	copy(pPtr,fPtr);
	//Display of First String//
	printf("\nCopy of first string is %s",f);
	//Input Index//
	printf("\nEnter an index location:");
	scanf("%d",&index);
	z=replace(pPtr,index);
	//Display string replacement//
	if(z==0)
	{	 
		printf("\nInvalid index\n");
	}
	else
	{
		printf("\nString after replacement operation is %s \n",pPtr);
	}
	//Input Second String//
	printf("\nEnter second string is (concatenate operation):");
	scanf("%s",x);
	//Display Second String//
	printf("\nSecond string is %s",x);
	concatenate(pPtr,xPtr,sPtr);//Combine two strings//
	//Display Merged String//
	printf("\nMerged string is %s\n",s);
	//input new string for prefix operation//
	printf("\nEnter a string(prefix operation):");
	scanf("%s",d);
	//input string prefix that want to be check//
	printf("Enter a string to check for prefix:");
	scanf("%s",e);
	//Display of the existance of prefix//
	if (prefix(dPtr,ePtr)==1)
	printf("\nString %s is a prefix of the string %s\n",e,d);
	else
	printf("\nString %s is not a prefix of the string %s\n",e,d);
	//Bonus Part//
	printf("\nBonus part\n");
	printf("\nEnter a string:");
	scanf("%s",b);
	printf("\nEnter a string to check for substring:");
	scanf("%s",c);
	if(substring(c,b)==0)	
	printf("Wrong");
	else
	printf("right");
	
	
}
int length(char *aPtr)//Calculating the length of string//
{	
	int counter=0;
	while(*aPtr!='\0')
	{
		counter++;
		aPtr++;
	}
	return counter;
}

int replace(char *s,int i )//Replacing index string to #//
{
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
void copy(char*pPtr,char*xPtr)//Copy string to another string//
{
	int counter=0;
	while(*pPtr!='\0')
	{
		*xPtr=*pPtr;
		counter++;
		pPtr++;
		xPtr++;
	}
	*xPtr='\0';
}
void concatenate(char*pPtr,char*xPtr,char*sPtr)//Merge two strings into one//
{
	while(*pPtr!='\0')
        {
                *sPtr=*pPtr;
                pPtr++;
                sPtr++;
        }
	while(*xPtr!='\0')
	{
		*sPtr=*xPtr;
		xPtr++;
		sPtr++;
	}
	*sPtr='\0';
}
				
int prefix(char*pPtr,char*xPtr)//Prefix Checking//
{
	int counter=0,counter2=0;
	while(*xPtr!='\0')
	{
		if(*xPtr==*pPtr)
		counter++;
		xPtr++;
		pPtr++;
		counter2++;
	}
	xPtr=xPtr-counter2;
	if (counter==length(xPtr))	
	return 1;
	else
	return 0;
}

int substring(char* a,char* b)
{
	int counter,counter2,count=0,lengtha,lengthb;
	lengtha=length(a);
	lengthb=length(b);
	for(counter=0;counter<lengthb;counter++)
	{
		while(*a==*b)
		{
			for(counter2=0;counter2<length(a);counter2++)
			{
				if(*(a+counter2)==*(b+counter2))
				count++;
				else
				break;
			}		
			break;
		}
		if(count==lengtha)
		break;
		else
		count=0;
		counter2=0;
		b++;
	}

	if (count==0)
	return 0;
	else
	return 1;

}


