


user = ["Sameer", "Vividh", "Shashank", "Raina", "Priyanshi", "Deboshi"]
print("Hii,My name is Ramu kaka")
name = input("What Your Name?\n").strip().capitalize()
if name in user:
    print("Hello {}".format(name))
    print("You Are allowed to log in")
    delete=input("Would you like to delete your data form database (y/n)\n").lower().strip()
    
    if delete=="y":
     user.remove(name)
     print(user)
    else:
        print("Ok, Thanks")

else:
    print("You Are not allowed to log in")
    add=input("{},would you like to add yourself to database(y/n)\n".format(name)).lower().strip()

    if add=="y":
        user.append(name)
        print("{},you are added to databse".format(name))
        show=input("Would you like to show list(y/n)\n").lower().strip()
        if show=="y":
            print(user)
        else:
            print("Ok no problem")
    else:
        print("Ok no problem, Have a Great day {}".format(name))

     
