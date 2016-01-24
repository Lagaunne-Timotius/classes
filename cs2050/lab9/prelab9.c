//Timotius Andrean Patrick Lagaunne
//14173082
//Labcode: TreeTrav319
#include "bst.h"
//Function headers
bst *createBST(int a[],int size);
void sort (int a[],int size);
bst *createMinBST(int a[],int start,int end);
void printGivenLevel(bst*root,int level);
int height(bst*root);

int main(int argc, char **argv)
{
	//Checking error
	if (argc < 2)
	{
		printf("usage: %s <input_filename>\n", argv[0]);
		return 0;
	}
	//Open file
	FILE *in = fopen(argv[1], "r");
	if (in == NULL) return 0;
	//Declaration of variable
	int i, size,level;
	//Scanning size from file
	fscanf(in, "%d", &size);
	//allocating memory for array
	int *array = malloc(size * sizeof(int));
	//Scanning number from the file
	for (i=0; i<size; i++)
		fscanf(in, "%d", &array[i]);
	//Declaring a node
	bst *root =NULL;
	//Creating BST
	root=createBST(array,size);
	//print in-order,pre-order,post-order tree traversal
	printf("Creating Binary Search Tree...\n");
	printf("In-order traversal: "); 
	printInorder(root); 
	printf("\n");
	printf("Pre-order traversal: ");
	printPreorder(root);
	printf("\n");
	printf("Post-order traversal: ");
	printPostorder(root);
	printf("\n");
	//Sort arrat
	sort(array,size);
	//Creatin binary tree with minimum level
	root=createMinBST(array,0,size-1);
	//printing BST
	printf("Minimum Height BST\n");
	printTree(root);
	//Bonus
	printf("Bonus.Please enter level of the tree:");
	scanf("%d",&level);
	if(level>height(root))
	printf("\nThe maximum height of this tree is %d",height(root));
	else
	printGivenLevel(root,level);

 return 0;
}


bst *createBST(int a[],int size)//Creating BST
{
		int i;
		bst *root = NULL; 
		for (i=0; i<size; i++)
                root = insert(root, a[i]);
		return root;
}
void sort (int a[],int size)//Sorting array
{
	int lh,temp,rh,counter;
	for(lh=0;lh<size;lh++)
	{	
		rh=lh;
		for(counter=lh;counter<size;counter++)
		{
			if(a[counter]<a[rh])rh=counter;
		}
		temp=a[lh];
		a[lh]=a[rh];
		a[rh]=temp;
	}
}
		
		
bst *createMinBST(int a[],int start,int end)//Creating BST with minimum level
{
		if (start > end) return NULL;
		int mid=(start+end)/2;
		bst *root = create_node(a[mid]);
               
		
		root->left=createMinBST(a,start,mid-1);
		
		root->right=createMinBST(a,mid+1,end);

 return root;
}

void printGivenLevel(bst*root,int level)//Printing given level
{
  if(root == NULL)
    return;
  if(level == 1)
    printf("%d ", root->val);
  else if (level > 1)
  {
    printGivenLevel(root->left, level-1);
    printGivenLevel(root->right, level-1);
  }
}


int height (bst*root)//finding the maximum level
{
   if (root==NULL)
       return 0;
   else
   {
     /* compute the height of each subtree */
     int lheight = height(root->left);
     int rheight = height(root->right);
 
     /* use the larger one */
     if (lheight > rheight)
         return(lheight+1);
     else return(rheight+1);
   }
} 

