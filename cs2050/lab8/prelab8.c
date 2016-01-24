//Timotius Andrean Patrick Lagaunne	
//14173082

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
typedef struct bt_{
	int value;
	struct bt_*right;
	struct bt_*left;
}BST;

BST* insert(BST* root,int value);
void displayBST(BST*root, int depth);
void printTree(BST*root);
void padding(char toPrint, int numTimes);

int main(void)
{
	int number,counter;
	BST* root=NULL;
	
	printf("Enter number:");
	scanf("%d",&number);
	root=insert(root,number);
	printf("Enter the number again?yes=1,no=0");
	scanf("%d",&counter);
	while(counter==1)
	{
		printf("Enter number:");
        	scanf("%d",&number);
        	root=insert(root,number);
		printf("Enter the number again?yes=1,no=0");
        	scanf("%d",&counter);
	}
	printTree(root);
	
}


BST* insert(BST* root,int value)
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


void displayBST(BST*root, int depth)
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

void printTree(BST*root)
{
	displayBST(root,0);
}
void padding(char toPrint, int numTimes)
{
	int i;
	for(i=0;i<numTimes;i++)
	printf("%c",toPrint);
}
