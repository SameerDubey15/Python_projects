import math


def add(x, y):
    print(x+y)


def sub(x, y):
    print(x-y)


def mult(x, y):
    print(x*y)


def div(x, y):
    print(x/y)


def log(x, y):
    s = math.log(x, y)
    print(s)


def sq(x, y):
    s = math.pow(x, y)
    print(s)


def root(x):
    s = math.sqrt(x)
    print(s)


def fact(x):
    s = math.factorial(x)
    print(s)


def remender(x, y):
    s = math.fmod(x, y)
    print(s)


def sin(x):
    s = math.sin(x)
    print(s)


def cos(x):
    s = math.cos(x)
    print(s)


def tan(x):
    s = math.tan(x)
    print(s)


def intan(x):
    s = math.atan(x)
    print(s)


def incos(x):
    s = math.acos(x)
    print(s)


def insin(x):
    s = math.asin(x)
    print(s)


def degtorad(x):
    s = math.radians(x)
    print(s)


def radtodeg(x):
    s = math.degrees(x)
    print(s)


opp = ["Addition",
       "Subtraction",
       "Multiplication",
       "Division",
       "Log",
       "Power",
       "Root",
       "Factorial",
       "Remainder",
       "Sin",
       "Cos",
       "Tan",
       "InverseSin",
       "InverseCos",
       "InverseTan",
       "Degree to Radian",
       "Radian to Degree"
       ]
print(*opp, sep="\n")
fun = input(
    "\n\nEnter the operation you want to do from the list of operations given above:  ").strip().lower()
if fun == "addition":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    add(x, y)
elif fun == "subtraction":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    sub(x, y)
elif fun == "subtraction":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    sub(x, y)
elif fun == "multiplication":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    mult(x, y)
elif fun == "division":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    div(x, y)
elif fun == "log":
    x = float(input("Enter the argument number: "))
    y = float(input("Enter the base number: "))
    log(x, y)
elif fun == "power":
    x = float(input("Enter the number: "))
    y = float(input("Enter power of that number: "))
    sq(x, y)
elif fun == "root":
    x = float(input("Enter the number: "))
    root(x)
elif fun == "factorial":
    x = float(input("Enter the number: "))
    fact(x)
elif fun == "remainder":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    remender(x, y)
elif fun == "sin":
    x = float(input("Enter the number: "))
    sin(x)
elif fun == "cos":
    x = float(input("Enter the number: "))
    cos(x)
elif fun == "tan":
    x = float(input("Enter the number: "))
    tan(x)
elif fun == "inversetan":
    x = float(input("Enter the number: "))
    intan(x)
elif fun == "inversecos":
    x = float(input("Enter the number: "))
    incos(x)
elif fun == "inversesin":
    x = float(input("Enter the number: "))
    insin(x)
elif fun == "degree to radian":
    x = float(input("Enter the number: "))
    degtorad(x)
elif fun == "radian to degree":
    x = float(input("Enter the number: "))
    radtodeg(x)
else:
    print("please check the spelling of operation or enter the valid operation")
