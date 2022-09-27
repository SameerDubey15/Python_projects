from random import choice


space=[" " for i in range(9)]

def board():
    row1 = "| {} | {} | {} |".format(space[0],space[1],space[2])
    row2 = "| {} | {} | {} |".format(space[3],space[4],space[5])
    row3 = "| {} | {} | {} |".format(space[6],space[7],space[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

while True:
    a=board()
    print(a)
    choose=int(input("Enter your move (1-9)").strip())
    if space[choose - 1] == " ":
        space[choose - 1]="X"
    else:
        print("That space is already taken")



