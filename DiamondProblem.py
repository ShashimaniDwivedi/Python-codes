class A:
    def method(self):
        print("Method in class A")
 
class B(A):
    def method(self):
        print("Method in class B")
 
class C(A):
    def method(self):
        print("Method in class C")
 
class D(B, C):
    pass
 
# Create an instance of class D
obj = D()
 
# Call the method inherited from class B
obj.method()
 
# Print the method resolution order (MRO)
print(D.mro())
 
