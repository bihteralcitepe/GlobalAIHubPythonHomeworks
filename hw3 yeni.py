name = input("I want to play a game! Please enter your name.")
print("Welcome ", name)

from random import choice

word = choice(["Phython", "Java", "C++", "Swift"])

guessed = []
wrong = []

tries = 2

while tries > 0:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        break

    print("PLEASE FIND THE WORD IN MY MIND", out)
    print(tries, "CHANCES LEFT")

    guess = input()

    if guess in guessed or guess in wrong:
        print("ALREADY GUESSED", guess)
    elif guess in word:
        print("10 POINTS FOR YOU!!")
        guessed.append(guess)
    else:
        print("THAT CANNOT BE TRUE...")
        tries = tries - 1
        wrong.append(guess)

    print()

if tries:
    print("You guessed", word)
else:
    print("YOU LOSE. EXIT THE GAME.")

