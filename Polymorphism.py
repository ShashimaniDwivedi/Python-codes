# Run time Polymorphism(Dynamic Binding)
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


# Create instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()


# Define a function that takes any animal and makes it speak
def make_animal_speak(animal):
    return animal.speak()


# Use the function with different animal objects
print(make_animal_speak(dog))  # Outputs "Woof!"
print(make_animal_speak(cat))  # Outputs "Meow!"
print(make_animal_speak(cow))  # Outputs "Moo!"

# Compile time Polymorphism(Static Binding)
'''
In Python, compile-time polymorphism,
 also known as method overloading,
  is not directly supported as 
  it is in some other languages
   like Java or C++. 
   In those languages, 
   you can define multiple functions
    or methods with the same name
     but different parameter 
     types or counts,
      and the correct method
       to be called is determined
        at compile time
         based on the arguments passed.

In Python, method overloading 
with different parameter
 types or counts is
  not natively supported.
   When you define multiple functions
    with the same name,
     only the most recent 
     definition of the function
      with that name is retained,
       effectively overwriting 
       the previous ones.
        However, you can achieve method
         overloading in Python
          using default arguments
           or variable-length argument lists.
'''


class Example:
    def add(self, a=None, b=None):
        if a is not None and b is not None:
            return a + b
        if a is not None:
            return a
        return 0


obj = Example()
print(obj.add(1, 2))  # Calls the version of add with two arguments
print(obj.add(1))  # Calls the version of add with one argument
print(obj.add())  # Calls the version of add with no arguments


# Operator Overloading
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # Overload the addition operator
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def __str__(self):
        # Define a custom string representation for the object
        return f"{self.real} + {self.imag}i"


# Create instances of ComplexNumber
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, 2)

# Use the overloaded + operator to add complex numbers
result = num1 + num2

# Display the result
print("Result:", result)  # Outputs "Result: 4 + 6i"


