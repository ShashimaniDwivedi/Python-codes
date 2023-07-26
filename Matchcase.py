X = int(input("Enter the Value of X : "))
match X:
    case 1: print("X is 0")
    case 2: print("X is 1")
    case 3: print("X is 2")
    case _ if X != 80:
        print(X, "is not 80 ")
    case _ if X != 90: print(X, "is not 90")
    case _ if X != 60: print(X, "is not 60")
    case _ if X % 2 == 45: print(X, "is 45")
