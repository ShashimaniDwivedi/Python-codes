marks=[12,45,32,98,11,13,34,66]
""" index=0
for mark in marks:
  print(mark)
  if(index==3):
    print("Student Topped in school")
  index+=1   """ 
  
for index, mark in enumerate(marks):
  print(index ,mark)
  if(index==3):
    print("Student Topped in school")
    
#chaanging starting index
for index, mark in enumerate(marks,start=1):
  print(mark)
  if(index==3):
    print("Student Topped in school")    
    
import pandas as pd
print(pd.__version__)
    