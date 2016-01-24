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

node* insert_top(node* head,int value);// Insert Link
void print(node* head);//print the link list
void delete(node* head,int value);// delete the memory allocation
int main (void)
{
	//Initialize and declaration of pointer	
	node *starPtr=NULL;
	node *n=NULL;
	//declaration of variable
	int value,counter;
	for(counter=0;counter<5;counter++)
	{	
	printf("Insert:");
	scanf("%d",&value);
	n=insert_top(starPtr,value);
	print(n);
	}
	for(counter=0;counter<3;counter++)
	{
	printf("Delete:");
        scanf("%d",&value);
	delete(starPtr,value);
	print(starPtr);
	}
	node* del;
	while(starPtr!=NULL)
	{
		del=starPtr;
		starPtr=starPtr->next;
		free(del);
	}
}
node* insert_top(node* head,int value)// Insert Link
{
	node *newPtr=malloc(sizeof(node));
	if (newPtr!=NULL)
	{
		newPtr->value=value;
		newPtr->next=head;
		head=newPtr;
	}
	else
	{
		printf("No memory available");
	}
	return head;
}
void print(node* head)//print the link list
{
 	node *currentPtr=head;
        while(currentPtr!=NULL)
        {
                printf("%s->",currentPtr->value);
                currentPtr=currentPtr->next;
        }
        printf("NULL\n");
}
void delete(node* head,int value)// delete the memory allocation
{
	node *currentPtr=head;
	node *PreviousPtr;
	while (currentPtr->value !=value) 
	{
		PreviousPtr=currentPtr;
		currentPtr = currentPtr->next;
		
	}
	PreviousPtr->next=currentPtr->next;
	free(currentPtr);
 }



