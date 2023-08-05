class Employee:
  def __init__(self,name):
    self._name = name
    
a=Employee("Harry")
# print(a.__name)  throw Error
print(a._Employee__name) 
print(a._name) 