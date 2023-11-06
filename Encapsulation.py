class Student:
    __name = None
    __roll_no = 0

    def set_name(self, name):
        self.__name = name

    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no


# Create an instance of the Student class
student = Student()
student.set_name("Manas")
re = student.get_name()
print("Name is : ", re)
student.set_roll_no(47)
re1 = student.get_roll_no()
print("Roll no is : ", re1)
print(student._Student__name)# Name Mangling Accessing indirectly Private member


