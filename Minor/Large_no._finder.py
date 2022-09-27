num=[]
enternum=int(input("Enter how many no. to be Inserted\n"))
for i in range(enternum):
    l=float(input(f"Enter {i+1}st number: "))
    num.append(l)
big=num[0]
p=0
for i in range(enternum):
    if num[i]>big:
        big=num[i]
        p=i+1
print("The largest element is ",big," which is found at position ",p)
