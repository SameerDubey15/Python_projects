num = int(input("Enter the number\n"))
prime = 1
for i in range(2, num//2 + 1):
    if (num%i==0):
        prime = 0
        break
if (prime == 1):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

