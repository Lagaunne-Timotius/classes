#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "stack.h"

#define MAX_EQU_LEN 100

/*
 * Returns a number corresponding the the preccedence 
 * of different arithmetic operators. * has a higher 
 * precedence that / which is greater than %, +, -
 * in that order. Higher precedence should return a higher
 * number so say 5 for * 1 for - and 0 for a non operator
 */
static char prec(char operator) {
	switch(operator)//Giving value for each operator
	{
		case '*':
		return 3;
		case '/':
		return 3;
		case '%':
		return 3;
		case '+':
		return 2;
		case '-':
		return 2;
		default:
		return 1;
	}
}


/*
 * Returns 1 if the string passed is an inteter
 * 0 otherwise
 */
static int isNumeric(char *num) {
	if(isdigit(*num))//Checking the value
	return 1;
	else
	return 0;
	
}

/*
 * converts a valid infix expression into postfix
 * Hint put a space between numbers and operators 
 * so you can use strtok in evaluate_postfix
 * ex: get 7 8 + vs 78+
 *
 * This is done with the following algorithm
 *
 * for each token in the string
 *     if the next token is a number
 *         append it to the postfix string
 *     else if the next token is a left paren
 *          push it onto the stack
 *     else if the next token is a right paren
 *          while the stack is not empty and the left paren is not at the top of the stack
 *              pop the next operator off of the stack
 *              append it to the postfix string
 *          pop the left paren off of the stack and discard it
 *     else if the next token is an operator (+, -, *, /)
 *         while the stack is not empty and the operator at the top of the stack has a higher precedence than the token
 *              pop the top element off of the stack and append it to the postfix string
 *         push the current token onto the stack
 *
 * while there are elements remaining on the stack
 *     pop the top element off of the stack and append it to the postfix string
 */
char* infix_to_postfix(char* infix) {
	//Declaration of variables	
	char *postfix;
	char *original;
	postfix=malloc(sizeof(char)*MAX_EQU_LEN);	
	original=postfix;
	stack *s=create_stack();
	
	//Converting to postfix
	while((*infix)!='\0')
	{
		if(isNumeric(infix))
		{
			(*postfix)=(*infix);
			postfix++;
			(*postfix)=' ';
			postfix++;
		}
		if((*infix)=='(')
		push(s,(*infix));
		if((*infix)==')')
		{
			while(isEmpty(s)==0&&top(s)!='(')
			{
				(*postfix)=top(s);	
				pop(s);
                        	postfix++;
				(*postfix)=' ';
                        	postfix++;
			}
			pop(s);

		}

		if(prec(*infix)!=1)
		{
			while(isEmpty(s)==0&&(prec((top(s)))>prec(*infix)))
                        {
                                (*postfix)=top(s);
				pop(s);
                                postfix++;
				(*postfix)=' ';
                        	postfix++;
		
                        }
			push(s,(*infix));
                       	
		}
		infix++;
	}
	while(isEmpty(s)==0)
	{
		(*postfix)=top(s);
                pop(s);
		postfix++;
		(*postfix)=' ';
                postfix++;

	}
	postfix--;
	(*postfix)='\0';
	
	return original;
}

/*
 * This function takes in a valid postfix expression
 * and evaluate it to an integer
 *
 * for each token in the string
 *      if the token is numeric
 *          convert it to an integer
 *          push it onto the stack
 *      else
 *          pop the top 2 element off of the stack
 *          the first goes into the right variable
 *          the second goes into the left variable
 *          apply the operation: 
 *              result = left op right
 *              ex result = left + right
 *
 *          push the result onto the stack
 *          
 * return the rsult from the stack
 */

int evaluate_postfix(char* postfix) { 
	
	//Declaration of variables
	char *token=strtok(postfix," ");
	stack *s=create_stack();
	int right,left;
	int result;
	//calculating by each token
	while((token)!=NULL)
	{	
		if(isNumeric(token))
			push(s,atoi(token));
		else
		{
			right=top(s);
			pop(s);
			left=top(s);
			pop(s);
			switch(*token)
			{
				case '*':
                		result=left*right;
				break;
                		case '/':
                		result=(int)left/right;
				break;
                		case '%':
                		result=left%right;
				break;
                		case '+':
                		result=left+right;
				break;
                		case '-':
                		result=left-right;
				break;
                		default:
                		break;
			}
			push(s,(int) result);
		}
	
		token=strtok(NULL," ");
	}
	return top(s);
}
			



