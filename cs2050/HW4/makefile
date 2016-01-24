all	   =   hw4
CC     =   gcc
CFLAGS =  -Wall -g

$(all): frontend.o calculator.o stack.o
	$(CC) $(CLFAGS)  frontend.o calculator.o stack.o -o $@

frontend.o: frontend.c calculator.h stack.h
	$(CC) $(CFLAGS) frontend.c -c -o $@

calculator.o: calculator.c calculator.h
	$(CC) $(CFLAGS) calculator.c -c -o $@

stack.o: stack.c stack.h
	$(CC) $(CFLAGS) stack.c -c -o $@
	
clean: 
	rm *.o hw4
