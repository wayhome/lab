cdef extern from "mycode.h":
    cdef int myfunc (int, int)

def callCfunc(int x, int y):
    print myfunc(x, y)
