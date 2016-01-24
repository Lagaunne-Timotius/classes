#include <stdlib.h>
#include "stack.h"

/* 
 * Creates an empty stack and sets
 * the size equal to 0
 */

stack* create_stack() {
	//Creating stack
	stack *s=malloc(sizeof(stack));
	s->size=0;
	s->stack=NULL;
	
	return s;
}

/*
 * pushes the value into the top of the stack
 */ 
void push(stack *s, int val) {
    	//Pushing the stack
    node *n = malloc(sizeof(node));
    n->data = val;
    n->next = s->stack;
    s->stack = n;
    s->size++;
}

/*
 * pops the head of the stack
 * the value is not returned
 */
void pop(stack *s) {
	//Poping the top
	if(s->size==0)return;
	node *current=s->stack;
	s->stack=s->stack->next;
	free(current);
	s->size--;	
}



/*
 * returns the value at the top of the stack
 * the stack remains unchanged
 */
int top(stack *s) {
	//Determining the value on top
	if(isEmpty(s)==1)
	return 0;
	return s->stack->data;
}

/*
 * returns 1 if the stack is empty
 * 0 otherwise
 */
int isEmpty(stack *s) {
	//Checking whether the stack is empty
	if(s->size==0)
	return 1;
	else return 0;
}
