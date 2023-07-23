dict = {1: "Karan", 2: "Raj", 3: "Radhe", 4: "Hans"}
print(dict)
print(dict[1])  # it through error if name doesn't exist
print(dict.get(2))  # it doesn't through error if name doesn't exist
print(dict.keys())
print(dict.values())
print(dict.items())
for key in dict.keys():
    print(key)
    print(dict[key])
print("************")
for val in dict.values():
    print(val)
print("*************")
for key in dict.keys():
    print(f"The value corresponding to the key {key} is {dict[key]}")
# Dictioary method
