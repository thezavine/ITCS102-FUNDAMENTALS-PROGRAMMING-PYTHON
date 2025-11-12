

def activity2():
    b = 10
    print("The worth of a is ", b)

def activity4():
    name = input("Can you tell me your name? ")
    print("Konnichiwa", name , "Welcome to the Matrix")

def sum_odd():
    num_odd = 0
    for c in range(1, 12, 1):
        number = int(input(f"{c} - Type a number... "))
        if number % 2 != 0:
            num_odd += number
    print("The sum of all odd numbers is:", num_odd)
