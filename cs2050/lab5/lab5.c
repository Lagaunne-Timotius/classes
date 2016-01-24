//Timotius Andrean Patrick Lagaunne
//14173082
//Talyxd
//Lab code: Merge340


#include<stdio.h>
#include<string.h>

//Function prototype

int is_sorted(int array[], int length);
int binary_search(int array[],int key,int low, int high);
void merge_sort(int c[],int size);
void merge(int a[], int m, int b[],int n,int c[]);
void print(int array[],int length);
int main(int argc, char *argv [])
{
	//Checking the number of argument
	if(argc!=3)
	{
		printf("The argument is not enough");
		return 0;
	}	
	
//Declaration of variables
	int length;
	int counter=0,counter2;
	char change;
	
//Opening the file
	FILE *sample=fopen(argv[2],"r");
	
//Checking the data in the file
	if(sample==NULL)
	{	
		printf("No content\n");
		return 0;
	}
	
//Scaning the length of the file scanned
	fscanf(sample,"%d",&length);
	
//Declaring the array
	int Number[length];
	
//Scanning the number and inputing to the array
	while(1)
	{
		fscanf(sample,"%d",&Number[counter]);
		if(feof(sample))break;
		counter++;
	}
	
//Checking whether the array is sorted or not			
	counter=is_sorted(Number,length);
	if(counter==1)
	printf("The array is sorted\n");
	else
	printf("The array is not sorted\n");
	
//Merge sort
	printf("Calling mergesort\n");
	merge_sort(Number,length);
	
//Checking whether the array is sorted or not
	counter=is_sorted(Number,length);
	if(counter==1)
        printf("The array is sorted\n");
        else
        printf("The array is not sorted\n");
	
//Changing the data type	
	change=(char)atoi(argv[1]);
	counter2=(int)change;
	
//Binary search
	counter2=binary_search(Number,counter2,0,length-1);
	
//Output for whether the number search is found or not
	if(counter2==1)
	printf("%s was found\n",argv[1]);
	else
	printf("%s was not found\n",argv[1]);
	
//Closing the file
	fclose(sample);
	
//The sorted array output printing
	printf("\nThe sorted array\n");
	print(Number,length);
	return 0;
}

int is_sorted(int array[], int length)//To check whether the array is sorted or not
{
	
//Declaring the variables
	int temp, counter;
	
//Checking the value of array
	for(counter=0;counter<length-1;counter++)
	{
		if(array[counter]>array[counter+1])
		return 0;
	}
	return 1;
}

int binary_search(int array[],int key,int low, int high)//Searching key value by Binary search	
{
	
//Declaring the variable
	int middle;
	
//Checking the key value
	while (low <= high)
	{
		middle = (low + high) / 2;
		if ( key == array[middle] )  {	
		return 1;}
		else if ( key < array[middle] )   
		{high = middle - 1;}
		else 
		{low = middle + 1;}
	}
	return 0;

}

void merge_sort(int c[],int size)//Do merge sort on the array
{
	
//Base case
	if(size<2)
	return;
	
//Declaring the variables and the array
	int mid=(size)/2;
	int a[mid];
	int b[size-mid];
	int i,j;
	
//Dividing the array
	for(i=0;i<mid;i++)
		a[i]=c[i];
	for(j=mid;j<size;j++)
		b[j-mid]=c[j];
		
//Recursive merge sort
		merge_sort(a,mid);
		merge_sort(b,size-mid);
		
//Merge the array
		merge(a,mid,b,size-mid,c);
}

void merge(int a[],int m, int b[], int n, int c[])//Comparing array value and Merge the array
{
	
//Declaring the variables
	int i=0, j=0,k=0;
	
	while(i<m&&j<n)//Comparing the value of array and copying to array c
	{
		if(a[i]<b[j])
			c[k++]=a[i++];
		else
			c[k++]=b[j++];
	}
	
//copying the rest of array to the array c
	while(i<m)
		c[k++]=a[i++];
	while(j<n)
		c[k++]=b[j++];
}

void print(int array[],int length)//Print the array
{
	int i=0;
	for(i=0;i<length;i++)
	{
		printf("%d\n",array[i]);
	}
}

