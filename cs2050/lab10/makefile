all	   =   lab10
CC     =   gcc
CFLAGS =  -Wall -g

$(all): frontend.o parser.o parser.h
	$(CC) $(CLFAGS)  frontend.o parser.o -o $@

main.o: frontend.c parser.h
	$(CC) $(CFLAGS) frontend.c -c -o $@

parser.o: parser.c parser.h
	$(CC) $(CFLAGS) parser.c -c -o $@

clean: 
	rm *.o lab10
