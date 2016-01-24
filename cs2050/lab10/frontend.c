//Timotius Andrean Patrick Lagaunne
//14173082
//LAB CODE:STRTOKEN315
#include"parser.h"
#define MAX_LINE 250
#define MAX_NAME 25

int main(int argc,char*argv[])
{
	//Checking for the number of arguments
	if(argc!=2)
	{
		printf("Wrong number of Arguments");
		return;
	}
	//Open the file
	FILE *fp= fopen(argv[1],"r");		
	//Checking the file
	if(fp==NULL)
	return;
	//Declaration of variables
	int prevTokIsName=0;
	int words=0;
	char buffer[MAX_LINE];
	char firstName[MAX_LINE];
	//Scan the data and identified the token
	while(fgets(buffer,MAX_LINE,fp))
	{	

		buffer[strlen(buffer)-1]='\0';
		char *token=strtok(buffer," ");
		while(token!=NULL)
		{
		if(is_phone_number(token))
			printf("Phone number:%s\n",token);
		else if(is_date(token))
			printf("Date:%s\n",token);
		else if(is_email(token))
			printf("Email:%s\n",token);
		else if(looks_like_name(token))
			{
				if(prevTokIsName)
				{
					printf("Name:%s %s\n",firstName,token);
					prevTokIsName=0;
				}
				else
				{
					 prevTokIsName=1;
					 strcpy(firstName,token);
				}
			}
		
		else
			prevTokIsName=0;
		token=strtok(NULL," ");
		words++;
		}
	}
	//Close the file
	fclose(fp);
	//Output for number of words in the file
	printf("There are %d words in the file\n",words);
	return 0;
}



