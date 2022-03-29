import math
print("Calculator by johark! say Add, Subtract, Multiply, or Divide")
o = input()
if o == "Add":
    print("Type 2 Numbers to Add.")
    x = float(input())
    y = float(input())
    print(x+y)
elif o == "Subtract":
    print("Type 2 Numbers to Add.")
    x = float(input())
    y = float(input())
    print(x-y)
elif o == "Multiply":
    print("Type 2 Numbers to Add.")
    x = float(input())
    y = float(input())
    print(x*y)
elif o == "Divide":
    print("Type 2 Numbers to Add.")
    x = float(input())
    y = float(input())
    print(x/y)
else:
    print("Oops, something went wrong, try again!")
