
def greet(fx):
  def mfx(*args, **kwargs):
   print("How are you")
   fx(*args, **kwargs)
   print("Thanks for using this function")
  return mfx

@greet
def Hello():
  print("Hello World!")
# @greet==greet(Hello)()  
Hello()  
# @greet(*args, **kwargs) 

@greet 
def add(a,b):
  print(a+b)  
add(2,3)
#greet(add)(2,3)  

def div(a,b):
  print(a/b)
  
def smart_div(func):
  
  def inner(a,b):
    if a<b:
      a,b=b,a 
    return func(a,b)
  return inner  
    
div = smart_div(div)
div(2,4)    