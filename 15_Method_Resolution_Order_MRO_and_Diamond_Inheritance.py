class A:
    def show(self):
        print("Showing A class")

class B(A):
    def show(self):
        print("Showing B class")

class C(A):
    def show(self):
        print("Showing C class")

class D(B, C):
    pass

d1 = D()

d1.show()