//maximum line size
#define MAX_LINE_SIZE 20

//binary search tree Structure----/* DO NOT CHANGE */------
typedef struct BST {
	int value;
    int treeNum;
	struct BST* left;
	struct BST* right;
}BST;

//list of pointers to the root node----/* DO NOT CHANGE */------
typedef struct rootList {
	struct BST* root;
	struct rootList* next;
}rootList;

//BFS Queue Structure-----/* DO NOT CHANGE */-------
typedef struct bfsQ{
	struct BST* treeNode;
	struct bfsQ* next;
	
}bfsQ;

//Function Prototypes-------/* DO NOT CHANGE */------
void insert_BST(BST** root, int insertValue, int treeNum);
BST* createTreeNode(int nodeValue, int treeNum);
void printTrees(rootList* listHead);
void print_BST_inorder(BST* root);
void enqueue(bfsQ** qHead, BST* new_tree_node);
BST* dequeue(bfsQ** qHead);
void BFS (rootList* listHead, int searchValue);
void insert_rootList(rootList** listHead, BST* root);
void free_list(rootList** listHead);
void free_BSTs(BST* root);

