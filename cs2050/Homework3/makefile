all: bfs

bfs: driver_template.o algorithm_template.o
	gcc driver_template.o algorithm_template.o -o bfs

driver_template.o: driver_template.c header.h
	gcc driver_template.c -c

algorithm_template.o: algorithm_template.c header.h
	gcc algorithm_template.c -c

clean:
	rm *.o bfs
