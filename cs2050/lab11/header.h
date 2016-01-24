#include<stdio.h>
#include<stdlib.h>
#include<time.h>


int partition(int* arr, int start, int end, int (*compare)(int, int));
void quick_sort(int* arr, int start, int end, int (*compare)(int, int));
int b_search(int *arr, int data, int (*compare)(int, int), int start, int end);
int compareSmallerOnLeft(int num1, int num2);
int compareSmallerOnRight(int num1, int num2);
void print(int* arr, int length);

