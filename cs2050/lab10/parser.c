#include"parser.h"
#include<string.h>
#include<stdio.h>
int is_phone_number(char *word)//Checking for whether token is phone number
{
 	//Declaration of variable
	int i;
	//Checking the token
	if((*word)!='(')
	return 0;
	word++;
	for(i=0;i<3;i++)
	{
        	if(!(isdigit((*(word)))))
        	return 0;
        	word=word+1;
	}
	if((*word)!=')')
	return 0;
	word++;

	if((*word)!='-')
	return 0;
	word++;

	for(i=0;i<3;i++)
	{
	if(!(isdigit((*(word)))))
        return 0;
        word=word+1;
	}
	if((*word)!='-')
	return 0;
	word=word+1;

	for(i=0;i<4;i++)
	{
        	if(!(isdigit((*(word)))))
        	return 0;
        	word=word+1;
	}
	return 1;
}

int is_date(char*word)//Checking whether token is date
{
	//Declaration of Variable
	int m,d;
	//Checking the token
	if(!(isdigit(*word)))
	return 0;	
	//Checking the month
	m=atoi(word);	
	if(m>12)
	return 0;
	word=word+2;
	if((*word)!='/')
	return 0;
	word++;
	
	d=atoi(word);
	//Checking the date based on the month
	switch(m)
	{
		case 1:
		if(d>31)
		return 0;
		break;
		case 2:
                if(d>28)
                return 0;
                break;
		case 3:
                if(d>31)
                return 0;
                break;
		case 4:
                if(d>30)
                return 0;
                break;
		case 5:
                if(d>31)
                return 0;
                break;
		case 6:
                if(d>30)
                return 0;
                break;
		case 7:
                if(d>31)
                return 0;
                break;
		case 8:
                if(d>31)
                return 0;
                break;
		case 9:
                if(d>30)
                return 0;
                break;
		case 10:
                if(d>31)
                return 0;
                break;
		case 11:
                if(d>30)
                return 0;
                break;
		case 12:
                if(d>31)
                return 0;
                break;
		
		default:
		return 0;
	}
	
	return 1;
	
}
int looks_like_name(const char* word)//Checking whether token looks like name
{
	int length,counter;
	//Checking the capital letter
	if(!isupper((*word)))
	return 0;
	
	length=strlen(word);
	//checking the lower case letter
	for(counter=1;counter<length;counter++)
	{
		if(!islower(*(word+counter)))
		return 0;
	}
	return 1;
	
}
int is_email(char*word)//Checking whether token is like email
{
	char *s;
	//Checking whether string is alphabet or numeric
	while((*word)!='\0')
	{
		if((*word)=='@')
		break;
		if(!(isalnum(*word)))
		return 0;
		word++;
	}
	//Loop to go to the end of string
	while((*word)!='\0')
	{
		word++;
	}
	word--;
	s=word;
	//Checking the domain
	while((*s)!='\0')
        {
                if((*s)=='m')
                {	s--;
			if((*s)=='o')
			 {	s--;
				if((*s)=='c')
			 	{	s--;
					if((*s)=='.')	
					return 1;
				}
			}
		}
		s=word;
		if((*s)=='u')
                {       s--;
                        if((*s)=='d')
                         {      s--;
                                if((*s)=='e')
                                {       s--;
                                        if((*s)=='.')
                                        return 1;
                                }
                        }
                }
		s=word;
		if((*s)=='v')
                {       s--;
                        if((*s)=='o')
                         {      s--;
                                if((*s)=='g')
                                {       s--;
                                        if((*s)=='.')
                                        return 1;
                                }
                        }
                }

		return 0;
		
	}
	
	
               
}
	


