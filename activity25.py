from activity25_1 import *
from activity25_2 import * 
#Creating a Menu Options with while loop and functions 

ur_name = input("Hello, Can I know your name? ")

print(f"Welcome {ur_name}, to my Compiler Program")

continously = True

while continously == True:
    print("Choose your Program")
    print("Z - Activity2\nY - Activity4\nX - Activity16\nW - Activity21\nV - Triangle Program\nO - Out")

    select = input("Which program/code would you like to run? ").lower()

    if select == 'z':
        activity2()
        continue
    elif select == 'x':
        activity4()
        continue
    elif select == 'y':
        sum_odd()
        continue
    elif select == 'w':
        print("Factorial Program")
        num_odd = input("Type a number for factorial computation...")
        print(f"The factorial of {num_odd} is {some_triangle(num_odd)}")
        continue
    elif select == 'v':
        try:
            num = int(input("Enter a number for the triangle program: "))
            some_triangle(num)
        except ValueError:
            print("Please enter a valid integer.")

    elif select == 'o':
        print("System Exit")
        break
    else:
        print("Wrong Choice")
