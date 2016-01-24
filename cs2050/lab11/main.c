//Timotius Andrean Patrick Lagaunne
//14173082
//lab code :QSORT322

#include"header.h"

//Main function
int main(int argc, char *argv[])
{
	//Error checking
	if(argc!=3)
	{
		printf("Number of Arguments are incorrect");
		return 0;
	}
	//Declaration of variables
	FILE *in=NULL;
	FILE *search=NULL;
	int *array,*serch,index=0,counter=0,sort,length, x;
	int (*compare)(int,int);
	//Opening the file
	in=fopen(argv[1],"r");
	search=fopen(argv[2],"r");
	//Checking the files
	if(in==NULL)
	{
		printf("Error");
		return 0;
	
	}
	if(search==NULL)
        {
                printf("Error");
                return 0;
        }
	//Allocating the memory to the pointer
	serch=malloc(sizeof(int)*100);
	array=malloc(sizeof(int)*3);
	
	//Scanning the files
	fscanf(in,"%d",&length);

	while(1)
	{
	
		fscanf(in,"%d",&array[index]);
		if(feof(in))break;	
		index++;
	}
	
	while(1)
        {

                fscanf(search,"%d",&serch[counter]);
                if(feof(search))break;
                counter++;
        }
	//Printing the array	
	print(array,length);	
	//Sorting the array
	
	printf("Do you want to sort with smaller values on the right(1) or left(2)?");
	scanf("%d",&sort);
	while(sort!= 1 && sort!=2)
	{
		printf("Please enter 1 for smaller value on the right or 2 for smaller values on the left:");
		scanf("%d",&sort);
	}
	if(sort==1)
	compare=compareSmallerOnLeft;
	else
	compare=compareSmallerOnRight;
	
	quick_sort(array,0,length-1,compare);
	//Printing the sorted output
	print(array,length);
	//Closing the in file
	fclose(in);
	//Search
	for(index=0;index<counter;index++)
	{
		x=b_search(array,serch[index],compare,0,length-1);
		if(x==1)
		printf("%d was found in the array.\n",serch[index]);
		else
		printf("%d was not found in the array.\n",serch[index]);
	}
	//Closing the search file
	fclose(search);
	return 0;
}










