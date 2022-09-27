""" Name= Sameer Dubey
    Roll No.= 20119083
"""


def function(x):
    return (a*x*x*x)+(b*x*x)+(c*x)+d


def Dfunction(x):
    return (2*a*x*x)+(b*x)+c


def newtonRaphson(x):
    h = function(x)/Dfunction(x)
    while abs(h) >= 0.0001:
        h = function(x)/Dfunction(x)
        x = x-h
        print("x=", x)

    print("The value of the root is : ", "%.4f" % x)


say = print("let the function be f(x) = ax3 + bx2 + cx + d\n")
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))
d = float(input("Enter value for d: "))
guess = float(input("Enter initial guess,X0= "))
newtonRaphson(guess)
