
"python uses the MRO (Method resolution order) to protect the Diamond problem"
"great example"

class A:
    def do_thing(self):
        print('From A')


class B(A):
    def do_thing(self):
        print('From B')


class C(A):
    def do_thing(self):
        print('From C')


class D(C,B):#jisse phle inherit karegi jaise yhan C ko usi ko chalayegi
    pass


d = D()
d.do_thing()