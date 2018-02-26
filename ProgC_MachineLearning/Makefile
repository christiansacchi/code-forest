CC = gcc
CFLAGS = -Wall -I .
objects = Array2D.o Perceptron.o main.o
common_h = ArrayLib/Array2D.h ArrayLib/ArrayLib.h

# LINK UTILI
# http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/
# http://www.network-theory.co.uk/docs/gccintro/gccintro_16.html
# https://stackoverflow.com/questions/6222371/makefile-clean-on-windows

# gcc -Wall main.c Perceptron.c ArrayLib/ArrayLib.h ArrayLib/Array2D.c -o prc_01

# -=- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- -=- #

# -=- LINKAGGIO -=- #
main: $(objects)
	$(CC) $(CFLAGS) $(objects) -o $@

# -=- COMPILAZIONE -=- #
main.o: Perceptron.h $(common_h)

Perceptron.o: Perceptron.h $(common_h)

Array2D.o: ArrayLib/Array2D.c $(common_h)
	$(CC) $(CFLAGS) -c ArrayLib/Array2D.c

# -=- ALTRO -=- #
.PHONY : clean
clean:
	del /S -f *.o

# -=- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- -=- #
