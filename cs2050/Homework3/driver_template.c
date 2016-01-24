#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*This is needed in order to for us to use our functions located in algorithm.c
as well as our structures. Make sure you understand what this header file is here
for and why we include it outside of our driver.c file*/
#include "header.h"

/********************************** MAIN *****************************************
 
 parameters: int argc (total number of command line arguments.
             char*argv[] (an array that holds the command line arguments)
 returns: int value of success (0) or failure (1)
 
 -> Your main function should read two files from the command line:
    1.) argv[1] should read the file input.txt. This file will have
        integer values that you will use to insert into the binary search tree.
        -1 values indicate the end of the list for the current binary search tree.
        DO NOT INSERT -1 IN THE binary search treeS.
 
    2.) argv[2] should read the file search.txt. This file will have
        integer values that you will use to search the binary search tree using BFS
 -> Main will call the functions: insert_BST, insert_rootList and BFS.
 
*********************************************************************************/

int main (int argc, char*argv[])
{
   	if(argc!=3)
	{
		printf("More argument needed");
		return 0;
	}
	 
	FILE *input=fopen(argv[1],"r");
	FILE *search=fopen(argv[2],"r");
    	int insert,tree,treeNum=1;
	BST *root=NULL;
	rootList *rootl=NULL; 
	while(1)
	{
		fscanf(input,"%d",&insert);
		if(feof(input))break;
		
		if(insert==-1)
		{
			insert_rootList(&rootl,root);
                	root=NULL;
			treeNum++;
		}
		else
		{
			insert_BST(&root,insert,treeNum);
		}
		
	}
	
	printTrees(rootl);
	fclose(input);	
	fclose(search);
	//free_list(&rootl);
    return 0;

}
