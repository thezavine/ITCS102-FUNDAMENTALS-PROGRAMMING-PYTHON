import random

print("Guess the number")

random_num = random.randint(1, 10)
attempts = 0
continuous = True

while continuous == True:
    number = int(input("Input an integer number--> "))

    attempts += 1

    if number == random_num:
        print("WHOA! You guessed it RIGHT!!")
        print(f"Only took {attempts} attempts")
        break
    else:
        print("Oh no! You guessed it wrong")
        print("KEEP doing it")
        continue
