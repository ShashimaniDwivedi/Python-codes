x = [1, 2, 3]
print(dir(x))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print("****************************")

e = Person("Harry", 28)
print(e.__dict__)


print("****************************")
print(help(Person))