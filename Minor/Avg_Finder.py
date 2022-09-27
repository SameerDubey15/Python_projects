from audioop import avg


count=int(input("How many numbers to averaged?\n"))
i=0
sum=0
n=[]
while(i<count):
    num=float(input(f"Enter {i+1}st Number: "))
    n.append(num)
    sum=sum + num
    i=i+1

l=tuple(n)
averge=sum/count
print(f"The average of {l} is {averge} ")

