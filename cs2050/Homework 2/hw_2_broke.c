#include <stdlib.h>
#include <stdio.h>

#define MAX_FILE_LENGTH 20

typedef struct node_{
	int value;
	struct node_ next;
}Node; 

typedef Node* List;

int create_list(List**,FILE*);
void print_list(List*, int);
void free_list(List*, int);
int list_sum(Node*);
void insertion_sort(List*, int);

/* Main will read in an input file from the command line, 
if the file fails to open the program should prompt the user for a new file, 
at no point should the program quit. If the program reads in a new file name, 
it can be up to size MAX_FILE_LENGTH. 
From there the program should read in the file, print it out, sort it, 
print it out again and then free it. */
int main (int argc, char* argv[]){
	
	if(argc != 2){
		printf("Incorrect number of command line arguments\n");
		return 1;
	}
	
	FILE* fp = fopen(argv[0], "r");
	
	while(fp == NULL){
		char file[MAX_FILE_LENGTH];
		printf("Unable to open file, enter a new file name: ");
		scanf("%d", file);
		fp = fopen(file, "r");
	}
	
	List array;
	int length = create_list(array, fp);
	
	printf("Pre Sort\n");
	print_list(&array, length);

	insertion_sort(length, array);
	printf("\nPost Sort\n");
	print_list(array, length);
	
	return 0;
}

/*This function takes in a pointer to a list and a file pointer. 
The first line of the input file is the length of the array to be created.
Each subsequent line is composed of two numbers, an index and a value. 
The index is the index of the linked list where a node with the value of value should be inserted. 
So for example, if index = 0 and value = 3, and before the insertion array[0] = 1 -> 2 -> NULL, 
after the insertion array[0] = 3 -> 1 -> 2 -> NULL. This function returns the length of the array.*/
int create_list(List** array,FILE* fp){
	int length, i, index, value;
	
	fscanf(fp, "%d", &length);
	
	array = malloc(sizeof(Node));
	
	for(i = 0; i < length; i++)
		(*array)[i] = NULL;
		
	while(1){
		fscanf(fp, "%d %d", &index, &value);
		
		Node* node = new_node(value);

		node->next = array[index];

		array[index] = node;
	}
	
	return length;
}

/*Creates a new node of type Node, sets node->value = value and returns it. */
Node* new_node(int value){
	Node* node;
	node->value = value;
	node->next = NULL;
	
	return node;
}

/*Takes in the head to a single linked list and returns the sum of the values of each of its nodes. 
Ex: Node* head = 1 -> 2 -> 3 -> NULL then list_sum(head) = 6.*/
int list_sum(Node* head){

	return head->value + list_sum(head->next);
}

/*For each index in the array, print the index, the linked list it points to,
and the sum of its nodes. See the sample output for an example.*/
void print_list(List* array, int length){
	int i;
	
	for(i = 0; i < length; i++){
		Node* curr = array[i];
		
		printf(" -\n|%d| ", i);
		
		printf("%d ->", curr->value);
		
		curr = curr->next;
			
		printf("NULL = %d\n -\n", list_sum(array[i]));
	}

	return curr;
}

/*Sorts the array using insertion sort in ascending order by the sums of each linked list. */
void insertion_sort(List* array, int length){
	int* sum = malloc(sizeof(int) * length);
	int i, j, value;
	Node* node;
		
	for(i = 1; i < length; i++){
		value = sum[i];
		node = array[i];
		for(j = i; j > 0 && value < sum[j + 1]; j++)
		{
			sum[j] = sum[j - 1];
			array[j] = array[j - 1];
		}
	}
	
	printf("\n");
	free(sum);
}

/*Free all allocated memory.*/
void free_list(List array, int length){
	int i;

	while(curr != NULL){
		Node* prev = curr;
		curr = curr->next;
		free(curr);		
	}	
}
