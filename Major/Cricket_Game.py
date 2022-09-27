import random
name = input("What's your name?\n")
print(
    f"Welcome {name} to Hand Cricket Game🏏\n\nMyself Babu Rao😁\nLets start the game with toss\n")
# Toss process
toss = input("Select Heads/H or Tales/T:\t").capitalize()
comp = 0
if toss == "H":
    comp = "Tales"
elif toss == "T":
    comp = "Head"
tossno = int(input("Now lets start the toss\nPlz select number between 1-6:\t"))
compno = int(random.randint(1, 6))
print(f"Computer had selected {compno}\n")
tottoss = tossno+compno
print(f"Total sum of numbers {tottoss}\n")
sel = 0
compsel = 0
if (tottoss % 2 == 0):
    if toss == "H":
        print("Sorry you loss the toss\n")
        compsellist = ["Batting", "Balling"]
        compsel = random.choice(compsellist)
        print(f"Computer have selected {compsel}")
    elif toss == "T":
        sel = input(
            "Congo, you had won the toss\nSelect Batting or Balling\n").title()
elif (tottoss % 2 == 1):
    if toss == "T":
        print("Sorry you loss the toss")
        compsellist = ["Batting", "Balling"]
        compsel = random.choice(compsellist)
        print(f"Computer have selected {compsel}")
    elif toss == "H":
        sel = input(
            "Congo, you had won the toss\nSelect Batting or Balling\n").capitalize()

# Game start
    print(f"Game is starting\n\n\n\n")

print("-------------------------------------------first inning------------------------------------------\n\n\n\n".upper())
# if user win toss
run = 0
i = 0
if (sel == "Batting"):
    user = int(input("Enter first batting value between 1-6:\t"))
    computer = random.randint(1, 6)
    print(f"Computer have selected {computer} run\n")
    run = user
    i = i+1
    while (computer != user):
        user = int(input("Enter value between 1-6:\t"))
        print(f"You have selected {user} run\n")
        computer = random.randint(1, 6)
        print(f"Computer have selected {computer} run\n")
        run += user
        i = i+1
elif sel == "Balling":
    user = int(input("Enter first balling value between 1-6:\t"))
    computer = random.randint(1, 6)
    print(f"Computer have selected {computer} run\n")
    run = computer
    i = i+1
    while (computer != user):
        user = int(input("Enter value between 1-6:\t"))
        print(f"You have selected {user} run\n")
        computer = random.randint(1, 6)
        print(f"Computer have selected {computer} run\n")
        run += computer
        i = i+1
# if comp win toss
elif(compsel == "Batting"):
    user = int(input("Enter first balling value between 1-6:\t"))
    computer = random.randint(1, 6)
    print(f"Computer have selected {computer} run\n")
    run = computer
    i = i+1
    while (computer != user):
        user = int(input("Enter value between 1-6:\t"))
        print(f"You have selected {user} run\n")
        computer = random.randint(1, 6)
        print(f"Computer have selected {computer} run\n")
        run += computer
        i = i+1
elif compsel == "Balling":
    user = int(input("Enter first batting value between 1-6:\t"))
    computer = random.randint(1, 6)
    print(f"Computer have selected {computer} run\n")
    run = user
    i = i+1
    while (computer != user):
        user = int(input("Enter value between 1-6:\t"))
        print(f"You have selected {user} run\n")
        computer = random.randint(1, 6)
        print(f"Computer have selected {computer} run\n")
        run += user
        i = i+1
# Game over of first inning
if i == 1:
    print("Wickettttttttttt\n")
    run = 0
else:
    print("Wickettttttttttt\n")

if compsel == "Batting":
    print(f"Computer had made {run} runs\n")
elif compsel == "Balling":
    print(f"You had made {run} runs\n")
elif sel == "Batting":
    print(f"You had made {run} runs\n")
elif sel == "Balling":
    print(f"Computer had made {run} runs\n")
else:
    print("Runs required to win is 1 ")


# Second inning starts
if sel == "Batting":
    print(f"Total runs made by you is {run}")
    print("Comupter have to make ", run+1)
    x = "Now its computer's batting\n\n\n\n"
    print(x)
elif sel == "Balling":
    print(f"Total runs made by computer is {run}")
    print("You have to make ", run+1)
    x = "Now its your batting\n\n\n\n"
    print(x)
elif compsel == "Batting":
    print(f"Total runs made by computer is {run}")
    print("You have to make ", run+1)
    x = "Now its your batting\n\n\n\n"
    print(x)
else:
    print(f"Total runs made by you is {run}")
    print("Comupter have to make ", run+1)
    x = "Now its computer's batting\n\n\n\n"
    print(x)
runtomake = run+1
print("-------------------------------------------second inning------------------------------------------\n\n\n\n".upper())
run2 = 0
if x == "Now its computer's batting\n\n\n\n":
    user = int(input("Enter value between 1-6:\t"))
    print(f"You have selected {user} run\n")
    computer = random.randint(1, 6)
    print(f"Computer have selected {computer} run\n")
    run2 += computer
    while ((run2 <= runtomake) and (computer != user)):
        user = int(input("Enter value between 1-6:\t"))
        print(f"You have selected {user} run\n")
        computer = random.randint(1, 6)
        print(f"Computer have selected {computer} run\n")
        run2 += computer
        left = run-run2
        print(f"{left} runs to go")
if x == "Now its your batting\n\n\n\n":
    user = int(input("Enter value between 1-6:\t"))
    print(f"You have selected {user} run\n")
    computer = random.randint(1, 6)
    print(f"Computer have selected {computer} run\n")
    run2 += user
    while ((run2 <= runtomake) and (computer != user)):
        user = int(input("Enter value between 1-6:\t"))
        print(f"You have selected {user} run\n")
        computer = random.randint(1, 6)
        print(f"Computer have selected {computer} run\n")
        run2 += user
        left = run-run2
        print(f"{left} runs to go")


# Game over of Second inning
print("Wickettttttttttt\n")
if run2 > run:
    if x == "Now its your batting\n\n\n\n":
        print("Congo you had won the game🎉🎊\n\n")
    elif x == "Now its computer's batting":
        print("Sorry better luck next time☹️ \n\n ")
elif run2 < run:
    if x == "Now its your batting\n\n\n\n":
        print("Sorry better luck next time☹️\n\n")
    elif x == "Now its computer's batting":
        print("Congo you had won the game🎉🎊\n\n")
elif run2 == run:
    print("Its a DRAWWWW")

print("------------------------------------------GAME OVER------------------------------------------------------------")
