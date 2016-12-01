class A(object):
    def save(self):
        print "A"


class B(A):
    pass


class C(object):
    def save(self):
        print "C"


class D(B, C):
    pass

D().save()
