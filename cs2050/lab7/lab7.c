/*Name: Timotius Andrean Patrick Lagaunne
  ID:#14173082
  Lab code: stack212
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_EQU_LEN 100
//Structure
typedef struct node_ {
	char data; 
	struct node_* next;
}node;

typedef struct stack_ {
	unsigned int size;
	node* stack;
}stack;

stack* create_stack();
void push(stack*s,char val);
char top(stack*s);
void pop(stack*s);
int paren_match(char*equation);
int paren_and_brackets_match(char*equation);
int main (int argc, char*argv[])
{
	//Declaration of variables
	char *string = malloc(MAX_EQU_LEN);
        int number,number2;
	FILE *input=NULL;
	//Error Checking and open file
	if (argc != 2){
	printf("Incorrect Number of Command Line Arguments");
	printf("\nCorrect Usage ./a.out <input file>\n");
	return 0;
	}
	if((input = fopen(argv[1], "r")) == NULL)
	{
		printf("\nUnable to open file.\n");
		return 2;
	}
	
	//Reading file 
	while (1)
	{
		fscanf(input,"%s",string);
		if (feof(input)) break;
		number=paren_match(string);
		number2=paren_and_brackets_match(string);
		//Output
		if(number==1&number2==1)
		printf("For equation %s; Parensmatch:Bonus Brackets match\n",string);
		if(number=0&number2==1)
		printf("For equation %s; Parens do not match:Bonus Brackets do not match\n",string);
		if(number==1&number2==0)
                printf("For equation %s; Parensmatch:Bonus Brackets do not match\n",string);
		if(number==0&number2==0)
                printf("For equation %s; Parensmatch do not match:Bonus Brackets do not match\n",string);

	}	
	//Close file
	fclose(input);
}

stack* create_stack()//Create Stack
{
	stack*s=malloc(sizeof(stack));
	s->size=0;
	s->stack=NULL;

	return s;
}
void push(stack* s, char val)//Input the data and increase the stack size
{
	//Allocating memory
	node* n = malloc(sizeof(node));
	//push the data into the stack
        n->data=val;
       	n->next = s->stack;
	s->size++;
	s->stack=n;     
}

void pop(stack* s)//Take out the data and decrease the stack size
{
	//Checking the size and taking out the data if the size not zero
	if(s->size == 0) return;
	node* current=s->stack;
	s->stack=s->stack->next;
	free(current);
	s->size--;
}
char top(stack* s)//Checking what is the top data
{
		node*current=s->stack;
		return current->data;        			       
}
int paren_match(char* equation)//Checking the parentheses
{
		//Declaration 
		 stack *s=create_stack();
		 int i;
		
		 for(i=0;equation[i]!='\0';i++)
		 {
			if(equation[i]=='(')
			{	
				push(s,equation[i]);
			}
			if(equation[i]==')')
			{
				if(s->size==0)
				return 0;
				else
				pop(s);
			}
		}	        	
		//Output value
		if(s->size==0)
		return 1;
		else
		return 0;		        										
}
int paren_and_brackets_match(char*equation)//Bonus
{
	 	 stack *s=create_stack();
		 stack *p=create_stack();
                 int i;

                 for(i=0;equation[i]!='\0';i++)
                 {
                        if(equation[i]=='(')
                        {	if(p->size!=0)
				return 0;
                                push(s,equation[i]);
                        }
			if(equation[i]=='[')
                        {
                                if(s->size!=0)
				return 0;
				push(p,equation[i]);
                        }
			
			if(equation[i]==']')
                        {
                                if(p->size==0)
                                return 0;
                                else
                                pop(p);
                        }

                        if(equation[i]==')')
                        {
                                if(s->size==0)
                                return 0;
                                else
                                pop(s);
                        }
                }

                if((s->size==0)&(p->size==0))
                return 1;
                else
                return 0;
}
                                                                                                                    
                                                                                                                                            
                                                                                                                                                                            
                                                                                                                                                                                                   
                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
