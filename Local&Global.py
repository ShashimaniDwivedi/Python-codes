x=10

def myFunc():
  global x # this keyword is use to declare variable globally 
  x +=1
  y=5
  print(y)
  
myFunc()
print(x)  