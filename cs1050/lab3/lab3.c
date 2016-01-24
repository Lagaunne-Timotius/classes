/*Timotius Andrean Patrick Lagaunne
  TALYXD
  14173082
  9/9/2013
  Compile with -lm option
*/

#include<stdio.h>
#include<math.h>

int main (void)
{
        //Dectaration of variables//
        float amount1,amount2,rate,z;
        int year;
        //Inputting value of the amount//
        printf("Enter the amount:");
        scanf("%f",&amount1);
        //Error Checking//
        while (amount1<=0)
        {
                printf("Invalid amount enter the amount again:");
                scanf("%f",&amount1);
        }
	//Inputting value of the year 1-10//
	printf("\nEnter the year:");
        scanf("%d",&year);
	//Error Checking//
        while (year<=0 || year>=11)
        {
                printf("Invalid year enter the year again:");
                scanf("%d",&year);
        }
	//Inputting the value of interest rate//
	printf("\nEnter the interest rate:");
	scanf("%f",&rate);
	// Compound of Interest formula//
	z=(float)pow((1+(rate/100)),(float)year);
	amount2= z*amount1;
	//Output message//	
	printf("\nAmount after %d years with the interest rate of\n",year);
	printf("%.2f%% is $%.2f.\n",rate,amount2);
	printf("Interest earned is $%.2f\n",(amount2-amount1));
	return 0;
}
