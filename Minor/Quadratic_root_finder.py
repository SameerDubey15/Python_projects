import math 
print("The standard form of a quadratic equation is ax2+bx+c=0, where a,b and c are real numbers and a≠0")
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))
print(f"The quadratic equation {a}X2+{b}X+{c}=0 ")

d=(b*b)-4*(a*c)
if d==0.0:
    print("The roots are real and equal")
    r=-b/(2*a)
    print("The Root of equation is ",r)
elif d>0.0:
    print("The roots are real and distinct")
    r1=(b+math.sqrt(d))/(2*a)
    r2=(b-math.sqrt(d))/(2*a)
    print(f"The Root of equation is {r1} and {r2}")
elif d<0.0:
    print("The roots are imaginary")
    r1=-b/(2*a)
    r2=math.sqrt(-d)/(2*a)
    print(f"The Roots are {r1}+i{r2} and {r1}-i{r2} ")




