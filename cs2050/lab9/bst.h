//Timotius Andrean Patrick Lagaunne
//14173082
//TreeTrav319
#include <stdio.h>
#include <stdlib.h>
//Structure
typedef struct node{
	int val;
	struct node *left, *right;
} bst;
//Function headers
bst *create_node(int val);
bst *insert(bst *root, int val);
void printInorder(bst *root);
void printPreorder(bst *root);
void printPostorder(bst*root);

void printTree(bst* root);
void displayBST(bst* root, int depth);
void padding(char toPrint, int numTimes);

bst *create_node(int val)//Creating node
{
	bst *n = malloc(sizeof(bst));
		n->val=val;
		n->left = NULL;
		n->right = NULL;
	return n;
}

bst *insert(bst *root, int val)//Insert value to BST
{
	if (root == NULL)
		root = create_node(val);
	else
	{
		if (val < root->val)
			root->left = insert(root->left, val);
		else
			root->right = insert(root->right, val);
	}
 return root;
}

void printPreorder(bst *root)//Printing in preOrder position
{
	if(root!=NULL)
        {
		printf(" %d",root->val);
                if(root->left!=NULL)
                printPreorder(root->left);
                if(root->right!=NULL)
                printPreorder(root->right);
	
        }

}

void printInorder(bst *root)//printing in inorder position
{
	if(root!=NULL)
	{
		
		if(root->left!=NULL)
		printInorder(root->left);
			printf(" %d",root->val);
		if(root->right!=NULL)
		printInorder(root->right);
			
	}
}

void padding(char toPrint, int numTimes)
{
	if(root!=NULL)
        {

                if(root->left!=NULL)
                printInorder(root->left);
                        printf(" %d",root->val);
                if(root->right!=NULL)
                printInorder(root->right);

        }
	int i;
	for (i = 0; i < numTimes; i++)
		printf("%c", toPrint);
}

void printPostorder(bst *root)//Printing in postorder position
{
	 if(root!=NULL)
        {
		
                if(root->left!=NULL)
                printPostorder(root->left);
                        
                if(root->right!=NULL)
                printPostorder(root->right);
		printf(" %d",root->val);
        }
	
}



void displayBST(bst* root, int depth)//Displaying the bst
{
	if (root == NULL)
	{
		padding(' ', depth);
		printf("-\n");
		return;
	}

	displayBST(root->left, depth+4);
	padding(' ', depth);
	printf("%d\n", root->val);
	displayBST(root->right, depth+4);
}

void printTree(bst* root)//Printing the bst
{
	displayBST(root, 0);
}
