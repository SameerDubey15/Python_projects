num=int(input("Enter the numbers of real number that has to be multiplied\n"))
realno=[]
mul=1
for i in range(num):
    real=float(input("Enter the Real Number: "))
    realno.append(real)
    mul=mul*real

print(f"The product of {realno} is {mul}")