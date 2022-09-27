c = 0
p = 1.0
count = int(input("Enter the number of values: "))
while(c<count):
    x = float(input("Enter a real number: "))
    p = p * x
    c = c+1
    
gm = pow(p,1.0/count)
print("The geometric mean is: ",gm)
