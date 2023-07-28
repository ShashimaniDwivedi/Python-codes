import os 
folders=os.listdir("Data")
print(os.getcwd())
# os.chdir("C:/Python")#change directory
for folder in folders:
  print(folder)
  print(os.listdir(f"Data/{folder}"))

cmd='EnumerateFunction42.py'
os.system(cmd)  