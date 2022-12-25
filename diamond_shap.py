class A:
    x = 25
    def met(self):
        print("This is a method from class A")

class B(A):
    x = 7
    def met(self):
        print("This is a method from class B")

class C(A):
    x = 8
    def met(self):
        print("This is a method from class C")

class D(C, B):
    def met(self):
        print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()
print(d.x)
d.met()


