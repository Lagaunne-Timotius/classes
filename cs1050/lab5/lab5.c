/* Timotius Andrean Patrick Lagaunne
   TALYXD
   9 September 2013
   14173082
   Lab Code:23040046
*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
//Function prototypes//
int generateNumber();
void displayMenu();
int checkGuess(int guess,int answer);
void printResult(int result, int answer);
int errorCheck(int x);

int main(void)
{	
//Random number generator//
	srand(time(NULL));
//Declaration of the variables//
	int guess,answer,result,check,counter,counter2,counter3;
	printf("Attempt for the bonus\n");
	counter=1;
	counter2=0;
	counter3=0;
//The Toss Game loop//
	while(counter==1)
	{
		answer=generateNumber();
		displayMenu();
	//Inputting the guess//
		printf("\nEnter your guess:");
		scanf("%d",&guess);
	//Error Checking//
		check=errorCheck(guess);
		while(check==0)
		{
			printf("Invalid guess enter your choice again:");
        		scanf("%d",&guess);
			check=errorCheck(guess);
		}
	//Guess checking//
		result=checkGuess(guess,answer);
	//Printing output//	
		printResult(result,answer);
	//Trial and correct guesses counter//
		counter2=counter2+result;
		counter3++;
	//Option wheter to play again//
		printf("Do you want to play again?(1 yes,0 no)");
		scanf("%d",&counter);
	}
//Printing correct guesses, number of trial and the winning percentage of whole trial// 
	printf("\nYou have made %d correct guesses in %d tries\n",counter2,counter3);
	printf("Your winning percentage is %.2f%%\n",(float)counter2*100/counter3); 
}


int generateNumber()//Random Number Generator//
{
	int x;
	x=rand()%2;
	return x;
}

void displayMenu() //Choices Display//
{
	printf("\nPlease take a guess\n0:Head\n1:Tail\n");
		
}

int checkGuess(int guess,int answer)//Guess and answer Comparison//
{
	int y;
	if (guess==answer)
	y=1;
	else
	y=0;
	return y;
}

void printResult(int result,int answer)// Printing Result Output//
{
	if (result== 1 && answer==1)
	printf("\nYour choice was tail and it is a correct guess\n");
	if (result== 1 && answer==0)
        printf("\nYour choice was head and it is a correct guess\n");
 	if (result== 0 && answer==1)
        printf("\nYour choice was head and it is an incorrect guess\n");
 	if (result== 0 && answer==0)
        printf("\nYour choice was tail and it is an incorrect guess\n");
}

int errorCheck(int guess)//Guess Checking// 
{
	if ( guess!= 0 && guess!= 1)
	return 0;
	else
	return 1;
}






