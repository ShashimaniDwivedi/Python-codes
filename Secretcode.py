import random


def remove_append(string):
    if len(string) < 2:
        return string

    modified_str = string[1:] + string[0]

    # Add three random characters to the start of the string
    for i in range(5):
        modified_str = chr(random.randint(16, 122)) + modified_str+chr(random.randint(34, 122))
    return modified_str


def decoded(string):
    decoded = string[3:-3]
    decoded = decoded[-1]+decoded[:-1]
    return decoded


input_str = input("Enter String: ")
print("Converting your code into secret code...")
result = remove_append(input_str)
print("Encoded String:", result)
b = (input("Press A to Decode your secret code : "))
if (b == 'A'):
    print("Dcoding the encoded message...")
    decoded_str = decoded(result)
    print("Decoded String:", decoded_str)
    print("System Hacked!!!")
else:
    print("!!!!Wrong input Security Alert...")
    print("!!!!Program Terminated...")
