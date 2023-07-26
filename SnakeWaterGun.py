import random

class Error:
  
    class ValueNotInRangeError(Exception):
      
        def __init__(self, value):
            self.value = value

    @staticmethod
    def check_range(value):
      
        if not 0 <= value <= 2:
            raise Error.ValueNotInRangeError(value)

try:
    user = int(input("Enter 0 for Snake, 1 for Water, and 2 for Gun: "))
    Error.check_range(user)  #calling without object
    
except Error.ValueNotInRangeError as e:
    print("Value not in range Error: Please enter a Valid number.")
    exit()

def check(comp, user):
  
    if comp == user:
        return 0
      
    if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1
      
    return 1

comp = random.randint(0, 2)
score = check(comp, user)

print("You:", user)
print("Computer:", comp)

if score == 0:
  
    print("It's a draw")
    
elif score == -1:
  
    print("You Lose")
    
else:
  
    print("You Won")
