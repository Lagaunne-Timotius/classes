/*Name: Timotius Andrean Patrick Lagaunne
  ID:#14173082
  Lab code: REC217
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//Structure
typedef struct node{
	int value; 
	struct node *next;
}node;

node* insert_end(node* head,int data);// Insert data to the link list
void print_list(node* head);//print the link list
int search(node* head, int data);//search data in the link list
void factorial_list(node* head);//change the value in link list into factorial value
void delete_list(node* head);//delete the memory allocated
int factorial(int n);// finding factorial value

int main (int argc, char** argv)
{
	//Error Checking//	
	if (argc != 2){
        printf("Incorrect Number of Command Line Arguments, Please try again!\n");
        return 0;
        }
        else if (strcmp(argv[1], "input.txt")!=0)
        {
                printf("Unable to open file!\n");
                return 0;
        }
	//Open file
	FILE *input=fopen(argv[1],"r");
	//Declaration of variable and initialization of head of link list
	int number,look;
	node *head=NULL;
	//Scanning and inputting value to the link list
	while (1)
        {
		fscanf(input, "%d", &number); 
			if (feof(input)) 
			break;
		head=insert_end(head, number);
	}
	//Print the link list
	print_list(head);
	//Inputing value to be searched in the link list
	printf("Please enter a number to search for:");
	scanf("%d",&look);
	//Search the data value in the link list
	if((number=search(head,look))==1)
	printf("%d was found!\n",look);
	else
	printf("%d was not found!\n",look);
	//Changing the value in the link list into factorial value
	factorial_list(head);
	//Print the link list
	print_list(head);
	//Delete the memory allocated
	delete_list(head);
	//Closing the file
	fclose(input);
	return 0;
}
node* insert_end(node* head, int data)//Insert new node to the link list
{

	//Checking the  head
	if (head==NULL)
	{
	        node *newPtr=malloc(sizeof(node));//Allocating memory to the node
        	newPtr->value=data;
		newPtr->next=NULL;
		head=newPtr;
		return head;
	}
	else//Recursively go to the other node
		head->next=insert_end(head->next,data);

	return head;
}	
                                                                                                                                                        
void print_list(node* head)//print the link list
{
        if(head)
        {
                printf("%d->",head->value);
                print_list(head->next);
        }
	else
	        printf("NULL\n");
}

int search(node* head, int data)//Search the value in the link list
{
	if(head==NULL) return 0;
	
	else if(head->value==data)
			return 1;
	else
	return search(head->next,data);
	
}

void factorial_list(node* head)//Changing the value in the link list into its factorial
{
	if (head!= NULL)
	{
		head->value=factorial(head->value);
		factorial_list(head->next);
	}
}

void delete_list(node* head)//Delete the memory allocated
{
	if(head!=NULL)
	{
		delete_list(head->next);
		free(head);
	}
}
		
int factorial(int n)//Evaluate  the factorial value 
{
	if(n!=0)
	return n*factorial(n-1);
	else
	return 1;
}


