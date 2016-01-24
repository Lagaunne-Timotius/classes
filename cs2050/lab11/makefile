all	   =   sort
CC     =   gcc
CFLAGS =  -Wall -g

$(all): main.o function.o header.h
	$(CC) $(CLFAGS)  main.o function.o -o $@

main.o: main.c header.h
	$(CC) $(CFLAGS) main.c -c -o $@

function.o: function.c header.h
	$(CC) $(CFLAGS) function.c -c -o $@

clean: 
	rm *.o sort
