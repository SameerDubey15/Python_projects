import random
health=50
diff=int(input("enter difficulty from 1 to 3\n"))
portion_health=int(random.randint(25,50)/diff)
health= health + portion_health
print(health)