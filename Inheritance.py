# Single Inheritance
class Parent:
    def __init__(self):
        self._super_attribute = True
        print("This is the parent class")


class child(Parent):
    def __init__(self):
        super().__init__()  # it call parent class Constructor
        print("This is child class")
        print(self._super_attribute)


a = child()


# Multiple Inheritance
class Parent1:
    def method1(self):
        print("Method from Parent1")


class Parent2:
    def method2(self):
        print("Method from Parent2")


class Child(Parent1, Parent2):
    def method3(self):
        print("Method from Child")


# Create an instance of the Child class
child_obj = Child()

# Access methods from both parent classes
child_obj.method1()  # Calls method from Parent1
child_obj.method2()  # Calls method from Parent2
child_obj.method3()  # Calls method from Child


# Multilevel Inheritance
class Grandparent:
    def grandparent_method(self):
        print("Method from Grandparent")


class Parent(Grandparent):
    def parent_method(self):
        print("Method from Parent")


class Child(Parent):
    def child_method(self):
        print("Method from Child")


# Create an instance of the Child class
child_obj = Child()

# Access methods from the grandparent, parent, and child classes
child_obj.grandparent_method()  # Calls method from Grandparent
child_obj.parent_method()  # Calls method from Parent
child_obj.child_method()  # Calls method from Child


# Hierarchical Inheritance
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


# Create instances of different derived classes
dog = Dog()
cat = Cat()
cow = Cow()

# Use the speak method to get different sounds
print(dog.speak())  # Outputs "Woof!"
print(cat.speak())  # Outputs "Meow!"
print(cow.speak())  # Outputs "Moo!"


# Hybrid Inheritance
class A:
    def method_A(self):
        print("Method from class A")


class B(A):
    def method_B(self):
        print("Method from class B")


class C(A):
    def method_C(self):
        print("Method from class C")


class D(B, C):
    def method_D(self):
        print("Method from class D")


class E(D):
    def method_E(self):
        print("Method from class E")


# Create instances of the derived classes
e = E()

# Access methods from various classes in the hierarchy
e.method_A()  # Calls method from class A
e.method_B()  # Calls method from class B
e.method_C()  # Calls method from class C
e.method_D()  # Calls method from class D
e.method_E()  # Calls method from class E
