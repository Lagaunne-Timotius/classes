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
	char *name; 
	struct node *next;
}node;

node* insert(node* head,char* name);// Insert Link
node* create_node(char* name);//create new node
void print(node* head);//print the link list
void delete(node* head);// delete the memory allocation
int main (int argc, char**argv)
{
	//Error checking
	if (argc != 2){
	printf("Incorrect Number of Command Line Arguments");
	printf("\nCorrect Usage ./a.out <input file>\n");
	return 0;
	}
	else if (strcmp(argv[1], "input.txt")!=0)
	{
		printf("Unable to open file \"%s\"",argv[1]);
		return 0;
	}
	//Open file
	FILE *input=fopen(argv[1],"r");
	//Initialize and declaration of pointer	
	node *starPtr=NULL;
	//declaration of variable
	char name[MAX_NAME_LEN];
	//Reading file 
	while(fscanf(input,"%s",name)!=EOF){
	starPtr=insert(starPtr,name);
	} 
	//Closing file
	fclose(input);
	//Print the link list
	print(starPtr);
	//Delete the memory allocation
	delete(starPtr);
}

node* insert(node* head, char* name)//Insert new node
{
	
	node *newPtr=create_node(name);
	node *currentPtr= head;
	if(head==NULL)
	return head=newPtr;
	while (currentPtr->next !=NULL) 
	{
		currentPtr = currentPtr->next;
	}
	currentPtr->next = newPtr;
	return head;
 }
node* create_node(char* name)//create new node
{
	node *n = malloc(sizeof(node));
	n->name=malloc(sizeof(char)*MAX_NAME_LEN);
	strcpy(n->name,name);
	n->next=NULL;
	return n;
}
void print(node* head)//Print link list
{	
	node *currentPtr=head;
	while(currentPtr!=NULL)
	{
		printf("%s->",currentPtr->name);
		currentPtr=currentPtr->next;
	}
	printf("NULL\n");
}
void delete(node* head)//Delete memory allocation
{
	node *delete;
        node *currentPtr=head;
        while(currentPtr!=NULL)
        {
                delete= currentPtr;
		currentPtr=currentPtr->next;
		free(delete);
        }
}



