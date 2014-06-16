all:
	cython mycodecpy.pyx
	gcc -g -O2 -fpic -c mycode.c -o mycode.o
	gcc -g -O2 -fpic -c mycodecpy.c -o mycodecpy.o `python-config --cflags`
	gcc -shared -o mycodecpy.so mycode.o mycodecpy.o `python-config --libs`
