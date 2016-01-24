/*Name: Timotius Andrean Patrick Lagaunne
  ID:#14173082
  Lab code: LL319
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_NAME_LEN 20
//Structure
typedef struct node{
	int val; 
	struct node* next;
}Node;

node* insert(node* head,int value);// Insert the value
node* delete(node* head,int value);//delete the value
void mul_even(node* head,int multiplier);//multiply the even value by multiplier
void print(node* head);//print the link list
node* reverse(node* head);
int main (int argc, char*argv[])
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
	//Declaration of variables
	char initial, temp;
	int number;
	//Open file
	FILE *input=fopen(argv[1],"r");
	//Initialize and declaration of pointer to a struct	
	node *starPtr=NULL;
	//Reading file 
	while (1)
	{
	fscanf(input,"%c",&initial); fscanf(input,"%c",&temp);
		 if (feof(input)) break;
	fscanf(input, "%d", &number); fscanf(input,"%c",&temp);
	//Selection
	switch(initial)
	{
	case 'i'://insert the number scanned
	starPtr=insert(starPtr,number);
	printf("Inserting %d into the list\n",number);
	break;
	case 'd'://delete the number in the link list based on the number  scanned from the file 
	starPtr=delete(starPtr,number);
	printf("Deleting %d from the list\n",number);
	break;
	case 'm':// multiply the even number by the multiplier scanned from the file
	mul_even(starPtr,number);
	printf("Multiplying all even numbers by %d\n",number);
	break;
	default:
	break;
	} 
	//Print the link list
	print(starPtr);
	}
	//Closing file
	fclose(input);
	starPtr=reverse(starPtr);
	printf("Bonus: the List has been reversed\n");
	print(starPtr);
	
 	return 0;
}

node* insert(node* head, int value)//Insert new node
{
	
	node *newPtr=malloc(sizeof(node));//Allocating memory to the node
	//initializing value in the new struct
	newPtr->val=value;
	newPtr->next=NULL;
	//Declaring new variable with data type node
	node *currentPtr= head;

	//Control for head if the head is NULL
	if(head==NULL)
	return newPtr;
	//Control for non even numbers
	if(value%2!=0)
	{
		while (currentPtr->next !=NULL) 
			currentPtr = currentPtr->next;
	
		currentPtr->next = newPtr;
	 return head;
	}
	//Control for even numbers
	else
	{
	newPtr->next=head;
	head=newPtr;
	return head;
	}
 }
node* delete(node* head,int value)// Deleting number based on the assigned number from the file
{
        //Declaring new variables type node
	node *currentPtr=head;
        node *temp;
	//Control for head->value
	if(head->val==value)
	{
		temp=head;
		head=head->next;
		//deleting 
		free(temp);
	}	
	//Control for other beside head
        while ((currentPtr->val)!=value)
        {
                temp=currentPtr;
                currentPtr = currentPtr->next;
		if(currentPtr->next==NULL)
		return head;
        }
	//change what it appoints
        temp->next=currentPtr->next;
        //deleting
	free(currentPtr);
	return head;
 }
void mul_even(node*head, int value)
{ 	
	//Declaring the variable type node
	node *currentPtr=head;
	//Checking even number
        while(currentPtr)
        {
               	//Multiply the number by multiplier
		if ((currentPtr->val)%2==0)
	       		currentPtr->val = (currentPtr->val)*value;
               	//Change the pointer
		currentPtr=currentPtr->next;
        }
}
 
void print(node* head)//Print link list
{	
	//Declaring new variable type node
	node *currentPtr=head;
	//Checking the currentPtr and print the value
	while(currentPtr!=NULL)
	{
		printf("%d->",currentPtr->val);
		currentPtr=currentPtr->next;
	}
	//print NULL
	printf("NULL\n");
}

node* reverse(node* head)
{
	node* currentPtr;
	node* previousPtr=head;
	
	currentPtr=previousPtr->next;
	head=currentPtr->next;
	head->next=currentPtr;
	currentPtr->next=previousPtr;	
	previousPtr->next=NULL;
	return head;
}

