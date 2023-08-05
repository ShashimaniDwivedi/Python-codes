class Myclass :
  def __init__(self,value):
    self.value = value
  
  def show(self):
    print(f"Value is {self.value}")
  
  #Getters
  @property
  def ten_value(self):
    return 10*self.value
  
  #Setters
  @ten_value.setter
  def ten_value(self, value):
    self.value = value/10
    
  
obj =Myclass(10) 
obj.ten_value=67
print(obj.ten_value)
obj.show() 
    