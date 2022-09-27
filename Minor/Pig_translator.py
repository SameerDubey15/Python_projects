from ntpath import join


oword=input("Type the sentence\n").lower().strip()

words=oword.split()
newword=[]
for word in words:
    if word[0] in "aeiou":
        lword= word + "yay"
        newword.append(lword)
    else:
        volpos=0
        for letter in word:
            if letter not in "aeiou":
                volpos=volpos + 1
            else:
                break
        cons=word[:volpos]
        rest=word[volpos:]
        lword= rest + cons + "ay"
        newword.append(lword)

print(" ".join(newword))




