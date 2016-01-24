//Timotius Andrean Patrick Lagaunne	
//14173082
//Lab code:BT322

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//Structure
typedef struct bt_{
	int value;
	struct bt_*right;
	struct bt_*left;
}BST;
//Function prototype
BST* insert(BST* root,int value);//Insert number to BST
void displayBST(BST*root, int depth);//Display BST
void printTree(BST*root);//Print tree
void padding(char toPrint, int numTimes);
int search(BST*root,int value);//Search the number in BST
BST*findNearest(BST*root,int value);//Search the closest number

int main(int argc,char **argv)
{
	//Error Checking
	if(argc!=2)
	{
		printf("Number of command is incorrect");
	 	return;
	}
	FILE *input=NULL;
	if((input = fopen(argv[1], "r")) == NULL)
	{
		printf("\nUnable to open file.\n");
		return 2;
	}
	//Declaration of variable
	int number,counter;
	BST* root=NULL;
	//Scan the file and insert it to BST
	while(1)
	{
		fscanf(input,"%d",&number);
		if(feof(input))break;
		root=insert(root,number);
	}	
	//Print the BST	
	printTree(root);
	//Search
	printf("Enter a number to search for in tree:\n");
	scanf("%d",&number);
	counter=search(root,number);
	//Display about the search
	if(counter==0)
	printf("%d was not found",number);
	else
	printf("%d was found",number);
	//Bonus
	printf("\nBonus:Enter a number to search for in the tree:");
	scanf("%d",&number);
	root=findNearest(root,number);
	printf("The nearest number to %d is %d\n",number,root->value);
	
}


BST* insert(BST* root,int value)//Insert the number to BST
{
	if (root==NULL)
	{
		root=(malloc(sizeof(BST)));
		root->value=value;
		root->left=NULL;
		root->right=NULL;
		
	}
	else if (value<root->value)
	{
		root->left=insert(root->left,value);
	}
	else
	{
		root->right=insert(root->right,value);
	}

	return root;
}


void displayBST(BST*root, int depth)//Display
{
	if(root==NULL)
	{
		padding(' ',depth);
		printf("-\n");
		return;
	}
	
	displayBST(root->left,depth+4);
	padding(' ',depth);
	printf("%d\n",root->value);
	displayBST(root->right,depth+4);
}

void printTree(BST*root)//Print the BST
{
	displayBST(root,0);
}
void padding(char toPrint, int numTimes)
{
	int i;
	for(i=0;i<numTimes;i++)
	printf("%c",toPrint);
}

int search(BST*root,int value)//Searching the number in BST
{
	
	if(root==NULL)
	return 0;
	if(root->value==value)
	return 1;
	else if(value<root->value)
	return search(root->left,value);
	else if(value>root->value)
	return search(root->right,value);
	
	return 0;
}
BST*findNearest(BST*root,int value)//Bonus  to find the closet number in BST compare with asked value
{
	int number;
	
	if(abs(root->value-value)==0)
	return root;
	
	number=abs(root->value-value);
	if(root->left!=NULL)
	{
		if(abs(root->left->value-value)<number)
        	return findNearest(root->left,value);
	}
        if(root->right!=NULL)
	{
		if(abs(root->right->value-value)<number)
        	return findNearest(root->right,value);
	}	
	return root;

}

