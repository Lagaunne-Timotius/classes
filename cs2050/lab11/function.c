
#include "header.h"

int partition(int* arr, int start, int end, int (*compare)(int, int))//Partition
{
    srand(time(NULL));
    int pivotIdx = start + rand() % (end-start+1); //choose Pivot
    int pivot = arr[pivotIdx];
	int t = arr[pivotIdx];
	arr[pivotIdx] = arr[end]; 
	arr[end] = t; 
	
    pivotIdx = end;
    int i = start -1;
	int j;  

    for(j=start; j<end; j++)
    {
	int cmp = compare(arr[j], pivot); 
	if(cmp > 0)  
	{
		i = i+1;
		t = arr[i];
		arr[i] = arr[j];
		arr[j] = t;
        }
    }
   	t = arr[i+1]; 
	arr[i+1] = arr[pivotIdx];
	arr[pivotIdx] = t;

	return i+1;
}
 
void quick_sort(int* arr, int start, int end, int (*compare)(int, int))//quick sort
{
	int index;
    	if(start < end)
	{
		index=partition(arr,start,end,compare);
		quick_sort(arr,index+1,end,compare);
		quick_sort(arr,start,index-1,compare);

	}
}

int b_search(int *arr, int data, int (*compare)(int, int), int start, int end)//Binary search
{
	int middle;
	middle=(start+end)/2;
	
	
	while(start<=end)
	{
		middle=(start+end)/2;
		if(compare(data,arr[middle])==0)
		return 1;
		
		if(compare(data,arr[middle])==1)
		end=middle-1;
		else
		start=middle+1;
	}
		return -1;
}

int compareSmallerOnLeft(int num1, int num2)//Compare smaller on left
{
	if(num1==num2)
	return 0;
	else if(num1<num2)
	return 1;
	else
	return -1;
}

int compareSmallerOnRight(int num1, int num2)//Compare smaller on right
{
	if(num1==num2)
        return 0;
        else if(num1<num2)
        return -1;
        else
        return 1;

}

void print(int* arr, int length)//Printing the array
{
	int counter;
	for(counter=0;counter<length;counter++)
	{
		printf("%d ",arr[counter]);
		
	}
	printf("\n");
}
