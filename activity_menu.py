# >>-------------------------------------------------- ACTIVITY 1 - 28 ------------------------------------------------------------------------------<<

def activity1():
    print("------------>> THIS IS THE ACTIVITY 1 <<--------------------")
    print(" \t>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<")
    print("\t>\tHello World\t\t<")
    print(" \t>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<")


def activity2():
    print("------------>> THIS IS THE ACTIVITY 2 <<--------------------")
    name = input("What is your name? ")
    print("Hello", name, "Welcome to the Matrix")


def activity3():
    print("------------>> THIS IS THE ACTIVITY 3 <<--------------------")
    print("Happy\n\t\tDay, ")
    print("\t\tBSIT 1A \n from DLL")
    print("always\thelp people")
    print("The Quick Brown Fox Jumps Over the Lazy Meow meow.")


def activity4():
    print("------------>> THIS IS THE ACTIVITY 4 <<--------------------")
    name = input("Enter a string -> ")
    print("Your name has", len(name), "characters")


def activity5():
    print("------------>> THIS IS THE ACTIVITY 5 <<--------------------")
    something = input("Input something --> ")
    try:
        something_eval = eval(something)
        print("The data type of something is", type(something_eval))
        answer = 1 + something_eval
        print("The answer is", answer)
    except Exception:
        print("Cannot perform addition on that input. The data type is", type(something))


def activity6():
    print("------------>> THIS IS THE ACTIVITY 6 <<--------------------")
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    print("\nThe sum is", n1 + n2)
    print("The difference is", n1 - n2)
    print("The product is", n1 * n2)

    if n2 != 0:
        print("The quotient is", n1 / n2)
        print("The floor division is", n1 // n2)
    else:
        print("Cannot divide by zero.")

    print(f"{n1} exponent by {n2} is {n1 ** n2}")
    print("The remainder is", n1 % n2 if n2 != 0 else "Undefined")


def activity7():
    print("------------>> THIS IS THE ACTIVITY 7 <<--------------------")
    a = 15
    print("The value of a is", a)
    a += 15
    print("The value of a is", a)
    a = a + 15
    a += 18
    a += 55
    a *= 12
    a -= 5
    print("The final value of a is", a)


def activity8():
    print("------------>> THIS IS THE ACTIVITY 8 <<--------------------")
    b = 6
    a = 18
    name1 = 'Azeth'
    name2 = 'azeth'
    print(name1 != name2)
    print("b >= a ?", b >= a)


def activity9():
    print("------------>> THIS IS THE ACTIVITY 9 <<--------------------")
    username = 'azeth'
    password = 'animeislife'

    print("Username correct?", username == 'azeth')
    print("Both correct?", (username == 'azeth') and (password == 'animeislife'))
    print("Either correct?", (username == 'azeth') or (password == 'animeislife'))
    print("Not both correct?", not ((username == 'azeth') and (password == 'animeislife')))


def activity10():
    print("------------>> THIS IS THE ACTIVITY 10 <<--------------------")
    name = input("Input your name: --> ")
    isPWDstudent = input("Are you a pwd student (Yes/No) --> ").lower()
    fare = float(input("Enter fare --> "))

    if isPWDstudent == "yes":
        discount = fare * 0.25
        new_fare = fare - discount
        print(f"Hi {name}, pwd student discount is {discount}. Discounted fare is {new_fare}")
    else:
        print(f"Sorry {name}, you are not eligible for pwd student discount")


def activity11():
    print("------------>> THIS IS THE ACTIVITY 11 <<--------------------")
    temp = float(input("Enter temperature --> "))

    if 1 <= temp <= 19:
        print("Temperature outside is cold")
    elif 20 <= temp <= 30:
        print("Temperature outside is lukewarm")
    elif 31 <= temp <= 45:
        print("Temperature outside is warm")
    elif 46 <= temp <= 50:
        print("Temperature outside is hot")
    elif temp >= 51:
        print("Temperature outside is super hot")
    else:
        print("Temperature is below 1 degree")


def activity12():
    print("------------>> THIS IS THE ACTIVITY 12 <<--------------------")
    print('hello world')

    for _ in range(1, 10):
        print('hello world')

    for ikot in range(1, 27):
        print(ikot, '- yuzu loves to read and watch anime')


def activity13():
    print("------------>> THIS IS THE ACTIVITY 13 <<--------------------")
    num = 0
    for x in range(1, 11):
        number = int(input("Enter a number "))
        num += number
        print('The new value of is', num)
    print("Final sum:", num)


def activity14():
    print("------------>> THIS IS THE ACTIVITY 14 <<--------------------")
    for o in range(20, 0, -1):
        print(o, "yohohohoo!")


def activity15():
    print("------------>> THIS IS THE ACTIVITY 15 <<--------------------")
    #STRING FORMATTING
    #FULLNAME, AGE, CURRENT ADDRESS

    full_name = 'Azeth Arvine L. Brandes'
    age = '20'
    cu_add = 'Barangay 8, Lagos Street, Lucena City'

    print(f"My full name is {full_name}. I am {age} yrs old and I live in {cu_add}")

    #Multiplication by 8 using that number 4

    num = eval(input("Enter the number:  "))

#for x in range(1,9,1):
        #print(f"{num} x {x} = {num*x} ")

#input 7 numbers, get the summation of all the PRIME NUMBERS

    prime_sum = 0

    for y in range(1,7,1):
        num1 = eval(input(f"{y} - Enter a number --> "))

        if num1 % 2 == 1:
            prime_sum += num 

    print(f"The sum of all the PRIME numbers given is {prime_sum}")

def new_func():
    full_name = 'Azeth Arvine L. Brandes'



def activity16():
    print("------------>> THIS IS THE ACTIVITY 16 <<--------------------")
    for y in range(1, 27):
        print(y, end="---")
    print()


def activity17():
    print("------------>> THIS IS THE ACTIVITY 17 <<--------------------")
    for _ in range(1, 27):
        for a in range(1, 27):
            print(a, end=" ")
        print()


def activity18():
    print("------------>> THIS IS THE ACTIVITY 18 <<--------------------")
    for x in range(1, 11):
        for b in range(1, 11):
            print(b, end=' ')
        print("<< this is x -->", x)


def activity19():
    print("------------>> THIS IS THE ACTIVITY 19 <<--------------------")
    for x in range(1, 27):
        for _ in range(1, x):
            print("*", end=' ')
        print()


def activity20():
    print("------------>> THIS IS THE ACTIVITY 20 <<--------------------")
    for x in range(1, 12):
        for _ in range(12, x, -1):
            print("*", end="  ")
        print()


def activity21():
    print("------------>> THIS IS THE ACTIVITY 21 <<--------------------")
    while True:
        que = input("Are the books already back in their places? (yes/no) --> ").lower()
        if que == 'yes':
            print("Books are back. Continuing loop...")
        elif que == 'no':
            print("Stopping the loop.")
            break
        else:
            print("Invalid input.")


def activity22():
    print("------------>> THIS IS THE ACTIVITY 22 <<--------------------")
    import random

    print("Guess the number!")
    random_num = random.randint(1, 10)
    attempts = 0

    while True:
        number = int(input("Input an integer number --> "))
        attempts += 1

        if number == random_num:
            print("WHOA! You guessed it RIGHT!!")
            print(f"Only took {attempts} attempts")
            break
        else:
            print("Oh no! You guessed it wrong. KEEP trying!")


def activity23():
    print("------------>> THIS IS THE ACTIVITY 23 <<--------------------")
    year = ['2001', '2002', '2003', '2004', '2005', '2006']

    for y in year:
        print(f"{y}, December")

    birthdate = 'December 27, 2004'
    reversed_list = list(birthdate)
    reversed_list.reverse()
    print("Reversed birthdate as list:", reversed_list)


def activity24():
    print("------------>> THIS IS THE ACTIVITY 24 <<--------------------")

    def artist(name):
        print(f"WOAH! {name}, can I have an autograph?")

    def summation(a):
        total = sum(range(1, a + 1))
        print(f"The sum of numbers 1 to {a} is {total}")

    summation(18)
    summation(20)


# --------------------------- ACTIVITY 25 ---------------------------

def activity25_1_activity2():
    print("The worth of a is 10")


def activity25_1_activity4():
    name = input("Can you tell me your name? ")
    print("Konnichiwa", name, "Welcome to the Matrix")


def sum_odd():
    num_odd = 0
    for c in range(1, 12):
        number = int(input(f"{c} - Type a number... "))
        if number % 2 != 0:
            num_odd += number
    print("The sum of all odd numbers is:", num_odd)


def factorial(num):
    facto = 1
    for b in range(num, 0, -1):
        facto *= b
    return facto


def some_triangle(num):
    for i in range(1, num + 1):
        print("* " * i)


def activity25():
    print("------------>> THIS IS THE ACTIVITY 25 <<--------------------")
    ur_name = input("Hello, Can I know your name? ")
    print(f"Welcome {ur_name}, to my Compiler Program")

    while True:
        print("Choose your Program")
        print("Z - Activity25_1_activity2")
        print("Y - Activity25_1_activity4")
        print("X - Sum Odd Numbers Program")
        print("W - Factorial Program")
        print("V - Triangle Program")
        print("O - Out")

        select = input("Which program/code would you like to run? ").lower()

        if select == 'z':
            activity25_1_activity2()
        elif select == 'y':
            activity25_1_activity4()
        elif select == 'x':
            sum_odd()
        elif select == 'w':
            num_fact = int(input("Type a number for factorial computation... "))
            print(f"The factorial of {num_fact} is {factorial(num_fact)}")
        elif select == 'v':
            num_triangle = int(input("Enter a number for the triangle program: "))
            some_triangle(num_triangle)
        elif select == 'o':
            print("System Exit")
            break
        else:
            print("Wrong Choice")


def activity26():
    print("------------>> THIS IS THE ACTIVITY 26 <<--------------------")
    highschool_sub2 = {
        'easy to learn': 'English',
        'slightly hard to understand': 'Filipino',
        'Very hard but it is my favorite sub': 'Math',
        'Hard': 'Science',
        'VERY EASY': 'MAPEH',
        'I get sleepy listening to this': 'Araling Panlipunan'
    }
    print(highschool_sub2['VERY EASY'])


def activity27():
    print("------------>> THIS IS THE ACTIVITY 27 <<--------------------")
    print("Adding Data to dictionary")
    void = {}

    def print_manhwa():
        for c, d in void.items():
            print(f"CODE {c} >> TITLE << {d}")

    while True:
        keys = input("Enter the keys for this Manhwa ----> ")
        value = input("Enter any Manhwa title: ")
        void[keys] = value

        option = input("Do you still wanna keep reading some Manhwa? Y/N/P (Print) ---> ").lower()

        if option == 'y':
            print("Ongoing...")
        elif option == 'n':
            print("Program closes")
            break
        elif option == 'p':
            print_manhwa()
        else:
            print("Error in selection")


def activity28():
    import pygame #type: ignore
    import random
    import time

    pygame.init()

    width = 600
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)

    clock = pygame.time.Clock()
    speed = 10
    snake_block = 10
    font_style = pygame.font.SysFont(None, 30)

    def draw_snake(snake_list):
        for block in snake_list:
            pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

    def game_loop():
        game_over = False
        game_close = False

        x = width // 2
        y = height // 2
        x_change = 0
        y_change = 0

        snake_list = []
        length_of_snake = 1

        food_x = round(random.randrange(0, width - snake_block) / 10) * 10
        food_y = round(random.randrange(0, height - snake_block) / 10) * 10

        while not game_over:
            while game_close:
                screen.fill(black)
                msg = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
                screen.blit(msg, [width / 6, height / 3])
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_c:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -snake_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = snake_block
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -snake_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = snake_block
                        x_change = 0

            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            x += x_change
            y += y_change

            screen.fill(black)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

            snake_head = [x, y]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True

            draw_snake(snake_list)
            pygame.display.update()

            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - snake_block) / 10) * 10
                food_y = round(random.randrange(0, height - snake_block) / 10) * 10
                length_of_snake += 1

            clock.tick(speed)

        pygame.quit()
        input("Game over! Press Enter to exit...")

    game_loop()
