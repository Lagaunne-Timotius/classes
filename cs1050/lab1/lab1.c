/*Name : Timotius Andrean Patrick Lagaunne
  Pawprint : talyxd
  Date : 08/19/2013
  Lab code : 8192013
 */

#include<stdio.h>
int main(void)

{

int distance,speed;
float time;

printf("Enter the distance:\n");
scanf("%d",&distance);
while (distance<=0)
{printf("\nDistance should be positive"),
printf("\nEnter the distance again:");
scanf("%d",&distance);
}
printf("\nEnter the speed:");
scanf("%d",&speed);
while (speed<=0)
{printf("\nSpeed should be positive number"),
printf("\nEnter the speed again:\n");
scanf("%d",&speed);
}


time=(float)(distance*3600)/(speed*1600);

printf("\nFlight time of the plane is %f",time);

printf(" seconds\n");
return 0;
}


