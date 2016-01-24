/*Name: Timotius Andrean Patrick Lagaunne
  ID:#14173082
  Lab code: confusing
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
//Structure
typedef struct node{
	int value; 
	struct node *next;
}Node;

Node* insert_end(Node* head,int data);// Insert data to the link list
int linearSearch(int array[],int length, int key);//Linear search of the array
int nodeSearch(Node* head, int key);//search data in the link list
void free_Nodes(Node *head);//Free the allocated memory
void print_list(Node*head);
int main (int argc, char** argv)
{
	//Print the title
	printf("Linear Search1		Node Search1\n");
	// Declaration variables
	int counter=atoi(argv[1]),i;
	//Iteration for each file
	for(i=2;i<argc;i++)
	{	
		//Opening the file
		FILE *input=fopen(argv[i],"r");
		//Error condition
		if(input==NULL)
		{
			printf("Unable to open %s",argv[i]);
			continue;
		}
		//random key 
		int key=rand()%1000;
		//declaration of variables
		int a=0,number,length;
		//scanning the length
		fscanf(input,"%d",&length);
		//array declaration
		int array[length];
		//head node declaration
		Node*head=NULL; 
		//scanning the file and inputing to link list and array
		while (1)
        	{
                fscanf(input, "%d", &number);
                        if (feof(input))
                        break;
                head=insert_end(head, number);
		array[a]=number;
		a++;
        	}
		
		//timing
		clock_t start, end;
		start=clock();
		//Linear search	
		linearSearch(array,length,key);
		end=clock();
		double time=(double)(end-start)/CLOCKS_PER_SEC;
		//Print the time
		printf("%.10lf",time);
		start=clock();
		//Node search
		nodeSearch(head,key);
		end=clock();
		time=(double)(end-start)/CLOCKS_PER_SEC;
		//Print the time
		printf("		%.10lf\n",time);
		//closing the file
		fclose(input);
		free_Nodes(head);
	}
	
	return 0;
}
Node* insert_end(Node* head,int data)//Insert new node to the link list
{

	//Checking the  head
	if (head==NULL)
	{
	        Node *newPtr=malloc(sizeof(Node));//Allocating memory to the node
        	newPtr->value=data;
		newPtr->next=NULL;
		head=newPtr;
		return head;
	}
	else//Recursively go to the other node
		head->next=insert_end(head->next,data);

	return head;
}	
                                                                                                                                                        

int nodeSearch(Node* head, int data)//Search the value in the link list
{
	if(head==NULL) return 0;
	
	else if(head->value==data)
			return 1;
	else
	return nodeSearch(head->next,data);
	
}

int linearSearch(int array[],int length,int key)//Linear search of value in an array
{
	int counter;
	for(counter=0;counter<length;counter++)
	{
		if(array[counter]==key)
		return 0;
	}
	return 1;
}

void free_Nodes(Node*head)//free the allocated memory
{
	Node *temp,*current=head;
	
	while(current!=NULL)
	{
		temp=current;
		current=current->next;
		free(temp);
	}
	free(current);

}

