/*Name: Timotius Andrean Patrick Lagaunne
  ID:#14173082
  Lab code: LLIST2314
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_NAME_LEN 20
//Structure
typedef struct node{
	int value; 
	struct node *next;
}node;

node* insert(node* head,int value);// Insert Link
void print(node* head);//print the link list
int factorial(int n);
int main (void)
{
	//Initialize and declaration of pointer	
	node *starPtr=NULL;
	node *n=NULL;
	int fact;
	//declaration of variable
	int value=0,counter;
	while(value!=-1)
	{	
	scanf("%d",&value);
	if(value==-1)
	break;
	fact=factorial(value);
	starPtr=insert(starPtr,fact);
	print(starPtr);
	}
	return;
}
node* insert(node* head, int value)//Insert new node
{

        node *newPtr=malloc(sizeof(node));//Allocating memory to the node
        newPtr->value=value;
	newPtr->next=NULL;
	//initializing value in the new struct
        node *previous;
	node *temp;
	node *current=head;
	if(current==NULL)
	{
	head=newPtr;
	return head;
	}
	if((current->value) > value)
	{
		newPtr->next=current;
		head=newPtr;
		return head;
	}
	while(current->next!=NULL)
	{
		if (current->value < value)
		{
			previous=current;
			current=current->next;
		}
		if (current->value > value)
		{
		previous->next=newPtr;
                newPtr->next=current;
		break;
		}
	}
	if(current->next==NULL)
	current->next=newPtr;
	
	return head;
}	
	
	
	
	
                                                                                                                                                                
void print(node* head)//print the link list
{
 	node *currentPtr=head;
        while(currentPtr!=NULL)
        {
                printf("%d->",currentPtr->value);
                currentPtr=currentPtr->next;
        }
        printf("NULL\n");
}
int factorial(int n)
{
	if(n!=0)
	return n*factorial(n-1);
	else
	return 1;
}


