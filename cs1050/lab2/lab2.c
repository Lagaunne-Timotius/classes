/*
Timotius Andrean Patrick Lagaunne
talyxd
Section D
08/26/2013
  
*/

#include <stdio.h>
#include <math.h>

int main(void)
{
	//Variables declaration//
   	int firsta,seconda,thirda,suma;
   	int firstl,secondl,thirdl;
   	float area,p;
	// First Angle data input//
	printf("Attempting bonus part\n"); 
	printf("Enter the first angle:");
	scanf("%d",&firsta);
	//Error Checking//
	while(firsta<=0)
	{
		printf("Invalid angle enter the angle again:");
		scanf("%d",&firsta);
	}
	//Second Angle data input//
        printf("\nEnter the second angle:");
	scanf("%d",&seconda);
	//Error Checking//	 
	while(seconda<=0)
 	{
		printf("Invalid angle enter the angle again:");
		scanf("%d",&seconda);
	}
	//Third angle data input//
	printf("\nEnter the third angle:");
        scanf("%d",&thirda);
	//Error Checking//       
	while(thirda <=0)
        {
		printf("Invalid angle enter the angle again:");
        	scanf("%d",&thirda);
        }
	//Deciding type of triangle formed//          
	suma=firsta+seconda+thirda;
	if (suma!= 180)
   	{
		printf("\nThree angle do not form a triangle\n");
		return 0;
	}

	else if (firsta==90 || seconda==90 || thirda == 90)
		printf("\nThree angle form a right angle triangle\n");      
	else if (firsta>90 || seconda>90 || thirda > 90)
        	printf("\nThree angle form an obtuse  angle triangle\n");
	else if(firsta<90 && seconda<90 && thirda<90)
        	printf("\nThree angle form an acute angle triangle\n");

	printf("\nEnter the length of the first side:");
	scanf("%d",&firstl);
	printf("Enter the length of the second side:");
        scanf("%d",&secondl);
	printf("Enter the length of the third side:");
        scanf("%d",&thirdl);
	 
	//Calculation of p//	 
	p=((float)firstl+secondl+thirdl)/(2);
	//Calculation of the area of the triangle//	 
	area=sqrt(((float)p*(p-firstl)*(p-secondl)*(p-thirdl)));
	//Output message//
	printf("\nArea of the triangle is %.6f\n",area);

}



