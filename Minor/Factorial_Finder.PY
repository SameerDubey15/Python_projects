def factorial(num):
    if num==1:
        f=1
    else:
        f=num*factorial(num-1)
    return f
n=int(input("Enter the Number\n"))
fact=factorial(n)
print(f"The factorial of {n} is {fact}")