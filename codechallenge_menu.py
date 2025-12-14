#----------------------------------------------------->> MENU OF CODE CHALLENGES <<-------------------------------------------------------------------------

def codechallenge1():
    print(">>--------------------------------------------------------<<")
    print("|\t\t THIS IS THE CODE CHALLENGE 1\t\t  |")
    print(">>--------------------------------------------------------<<")
    name = input("What's your name: ")
    print("\t\t\t\t*\n\t\t\t*\t\t*\n\t\t*\t\t\t\t*\n\t*\t\t\tHI\t\t\t*\n*\t\t\t\tBRANDES\t\t\t\t*\n\t*\t\t\t\t\t\t*\n\t\t*\t\t\t\t*\n\t\t\t*\t\t*\n\t\t\t\t*")


def codechallenge2():
    print(">>--------------------------------------------------------<<")
    print("|\t\t THIS IS THE CODE CHALLENGE 2\t\t  |")
    print(">>--------------------------------------------------------<<")
    amount = int(input("Enter amount to deposit: "))

    a = amount // 1000
    amount %= 1000
    b = amount // 500
    amount %= 500
    c = amount // 200
    amount %= 200
    d = amount // 100
    amount %= 100
    e = amount // 50
    amount %= 50
    f = amount // 20
    amount %= 20
    g = amount // 10
    amount %= 10
    h = amount // 5
    amount %= 5
    i = amount // 1
    amount %= 1

    print("P1000:", a)
    print("P500 :", b)
    print("P200 :", c)
    print("P100 :", d)
    print("P50  :", e)
    print("P20  :", f)
    print("P10  :", g)
    print("P5   :", h)
    print("P1   :", i)


def codechallenge3():
    print(">>--------------------------------------------------------<<")
    print("|\t\tTHIS IS THE CODE CHALLENGE 3\t\t  |")
    print(">>--------------------------------------------------------<<")

    username = 'yuzuhzea'
    password = 'pretty'

    uname = input("Enter username: ")
    pinput = input("Enter password: ")

    if uname == username and pinput == password:
        print("Access Granted")
    else:
        print("Access Denied")


def codechallenge4():
    print(">>--------------------------------------------------------<<")
    print("|\t\t THIS IS THE CODE CHALLENGE 4\t\t  |")
    print(">>--------------------------------------------------------<<")
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")


def codechallenge5():
    print(">>--------------------------------------------------------<<")
    print("|\t\t THIS IS THE CODE CHALLENGE 5\t\t|  ")
    print(">>--------------------------------------------------------<<")
    print("This is Code Challenge 5")
    print("Welcome to the World of Manga Selection!")
    print("Answer some questions before we proceed.")

    genre = int(input('\n1. Action\n2. Comedy\n3. Horror\nAnswer: '))

    if genre == 1:
        print("Welcome to the list of Action Manga Recommendations: ")
    elif genre == 2:
        print("Welcome to the list of Comedy Manga Recommendations: ")
    elif genre == 3:
        print("Welcome to the list of Horror Manga Recommendations: ")
    else:
        print("Sorry! We don’t have that genre. Try another!")

    length = input("\nHow long should the manga be?\n1. Short\n2. Medium\n3. Long\nAnswer: ")

    if length == "1":
        print("You chose short. Now let's proceed to decades.")
    elif length == "2":
        print("You chose medium. Now let's proceed to decades.")
    elif length == "3":
        print("You chose long. Now let's proceed to decades.")
    else:
        print("Invalid choice, try again!")

    year = input("\nChoose decade:\n1. 1990s\n2. 2000s\n3. 2010s\nAnswer: ")

    if year == "1":
        print("You chose 1990s, nice!")
    elif year == "2":
        print("You chose 2000s, great!")
    elif year == "3":
        print("You chose 2010s, have fun!")
    else:
        print("Invalid choice, try again!")


def codechallenge6():
    print(">>--------------------------------------------------------<<")
    print("|\t\t> THIS IS THE CODE CHALLENGE 6 \t\t  |")
    print(">>--------------------------------------------------------<<")
    num = int(input("Input a number --> "))
    result = 1

    for x in range(num, 0, -1):
        print(result, "*", x, "=", result * x)
        result *= x

    print("Factorial is", result)


def codechallenge7():
    print(">>--------------------------------------------------------<<")
    print("|\t\tTHIS IS THE CODE CHALLENGE 7 \t\t   |")
    print("|\t\t>> ODD NUMBER SUMMATION <<\t\t   |")
    print(">>--------------------------------------------------------<<")

    result = 0
    for x in range(10):
        num = int(input("Enter a number: "))
        if num % 2 != 0:
            result += num

    print("The sum of all the ODD numbers is", result)


def codechallenge8():
    print(">>--------------------------------------------------------<<")
    print("|\t\t THIS IS THE CODE CHALLENGE 8\t\t  |")
    print(">>--------------------------------------------------------<<")
    num = int(input("Enter a number: "))

    print(f"\nMultiplication table for {num}:")
    for x in range(1, 11):
        print(num, "x", x, "=", num * x)


def codechallenge9():
    print(">>--------------------------------------------------------<<")
    print("|\t\t THIS IS THE CODE CHALLENGE 9\t\t  |")
    print(">>--------------------------------------------------------<<")
    tim = int(input("Enter the starting number for countdown: "))

    print("\nCountdown started:")
    for x in range(tim, 0, -1):
        print(x)
    print("LIFTOFF!!")


def codechallenge10():
    print(">>--------------------------------------------------------<<")
    print("|\t\tTHIS IS THE CODE CHALLENGE 10 \t\t  |")
    print(">>--------------------------------------------------------<<")
    print("\t\t\t   *", end=" ")
    for a in range(1, 15):
        for b in range(15, a, -1):
            print(" ", end=' ')
        for c in range(1, a):
            print("*", end=' ')
        for d in range(1, a):
            print("*", end=' ')
        print()


def codechallenge11():
    print("|\t\t THIS IS THE CODE CHALLENGE 11 |\t\t")
    for a in range(1, 11):
        for b in range(10, a, -1):
            print(" ", end=" ")
        for c in range(0, a):
            print("*", end=" ")
        for d in range(1, a):
            print("*", end=" ")
        for e in range(10, a, -1):
            print(" ", end=" ")
        print()

    for f in range(9, 0, -1):
        for g in range(10, f, -1):
            print(" ", end=" ")
        for g in range(0, f):
            print("*", end=" ")
        for i in range(1, f):
            print("*", end=" ")
        for j in range(10, f, -1):
            print(" ", end=" ")
        print()


def codechallenge12():
    print(">>--------------------------------------------------------<<")
    print("|\t\t THIS IS THE CODE CHALLENGE 12 |\t\t")
    print(">>--------------------------------------------------------<<")
    for e in range(1, 10):
        for f in range(10, e, -1):
            print(' ', end=" ")
        for g in range(e, 0, -1):
            print(g, end=" ")
        for h in range(2, e + 1):
            print(h, end=" ")
        print()


def codechallenge13():
    print(">>--------------------------------------------------------<<")
    print("|\t\t THIS IS THE CODE CHALLENGE 13 \t\t|")
    print(">>--------------------------------------------------------<<")

    for k in range(1, 9):
        for l in range(11, k, -1):
            print(" ", end=" ")
        for m in range(0, k):
            print("-", end=" ")
        for n in range(1, k):
            print("-", end=" ")
        print()

    for z in range(1, 6):
        for a in range(8, 0, -1):
            print(" ", end=" ")
        for b in range(4, 0, -1):
            print("|", end=" ")
        print()


def codechallenge14():
    print(">>--------------------------------------------------------<<")
    print("|\t\t THIS IS THE CODE CHALLENGE 14 \t\t|")
    print(">>--------------------------------------------------------<<")
    name = input("Hello! What is your name: ")
    print("<<------------------------------------------->>")

    result = 0
    odd = "" #More like a list
    start = True

    while start == True:
        num = eval(input("Please enter a number --> "))
        if num % 2 == 1:
            print("ODD number Detected")
            odd += str(num) + ","
            result += num
            continue
        elif num == 0: #it means that it will stop if user input 0
            print("The Loop has been Terminated")
            break
        else:
            if num % 2 == 0:
                print("Even number, leaping...")
            else:
                print("Error Number")
            continue
    print(f"Konnichiwa {name}, The total of all ODD numbers you input is {result}")
    print(f"All the odd numbers you input is {odd}")

def codechallenge15():
    print(">>--------------------------------------------------------<<")
    print("|\t\tTHIS IS THE CODE CHALLENGE 15 \t\t|")
    print(">>--------------------------------------------------------<<")
    print("List of Anime Titles")
    anime = []
    manga = True

    while manga:
        num = input("Enter the title of an Anime (type 'exit' to stop): ")
        if num.lower() == "exit":
            print("Anime entry program has exited successfully!")
            break
        anime.append(num)
        print(f"'{num}' has been added to your Anime List")

    print("Here are your anime titles:")
    for r in anime:
        print(f"- {r}")


def codechallenge16():
    print(">>--------------------------------------------------------<<")
    print("|\t\t THIS IS THE CODE CHALLENGE 16 |\t\t")
    print(">>--------------------------------------------------------<<")
    import os
    import json

    os.system('cls')

    print("IT students INFORMATION SYSTEM")
    print(">>>>>>>>>>>>>>>>>>>         <<<<<<<<<<<<<<<<<<<<<<<")

    ITstudent_records = {}

    while True:
        print("CHOOSE FROM THE CHOICES BELOW...")
        print("Z - Add Information\nY - Print the IT Student record")
        print("X - Find the information\nW - Remove the record")
        print("V - Modify the record\nU - Export IT Student record\nT - Import IT Student record")
        print("S - EXIT ")
        print("<<--------------------------------------------------------------->>")

        option = input("Your decision >>>> ").lower()

    # ADD INFORMATION
        if option == 'z':
            os.system('cls')
            print("Combining IT Information")
            print(">>>-------------------------------------------------->>")

            findthe_id = input("Key (COURSE-ID) ---->> ").lower()

            firstname = input("Type the First Name.... ").upper()
            lastname = input("Type the Last Name.... ").upper()
            year = input("Type the Year: ").upper()
            email = input("Type the Email: ").upper()
            status = input("Type the Status: ").upper()
            age = input("Type the Age: ").upper()
            home_address = input("Type the Home address: ").upper()

            ITstudent_records[findthe_id] = [firstname, lastname, year, email, status, age, home_address]
            print("<----------------Information Saved-------------------->")
            continue

    # PRINT ALL RECORDS
        elif option == 'y':
            os.system('cls')
            print("PRINTING STUDENT RECORDS")

            for id, record in ITstudent_records.items():
                    print(f"IT STUDENT ID {id} in STUDENT RECORD {record}")
                
            continue

    # FIND RECORD
        elif option == 'x':
            os.system('cls')
            print("Look for IT Student Record... ")

            findthe_id = input("Type the ID to find >>> ").lower()

            if findthe_id in ITstudent_records:
                print("---------------------->>>><<<<<---------------------")
                print("\tThe Record has been found!")
                ("---------------------->>>><<<<<---------------------")

                for a in ITstudent_records[findthe_id]:
                    print(f" >> {a}")
            else:
                print("---------------------->>>><<<<<---------------------")
                print("\tNo record found :< ")
                print("---------------------->>>><<<<<---------------------")
            continue

    # REMOVE RECORD
        elif option == 'w':
            os.system('cls')
            print("REMOVE THE EXISTING RECORD")

            findthe_id = input("Type the ID to search >>> ").lower()

            if findthe_id in ITstudent_records:
                print("---------------------->>>><<<<<---------------------")
                print("\tThe Record has been found:")
                print("---------------------->>>><<<<<---------------------")
                for a in ITstudent_records[findthe_id]:
                    print(f" >> {a}")

                ITstudent_records.pop(findthe_id)
                print("---------------------->>>><<<<<---------------------")
                print("\tThe record has been deleted.")
                print("---------------------->>>><<<<<---------------------")
            else:
                print("---------------------->>>><<<<<---------------------")
                print("\tNo record found.")
                print("---------------------->>>><<<<<---------------------")
            continue

    # MODIFY RECORD
        elif option == 'v':
            os.system('cls')
            print("EDIT / MODIFY STUDENT RECORD")
            print(">>>-------------------------------------------------->>")

            findthe_id = input("Type the ID to find >> ").lower()

    # Check if ID exists
            if findthe_id not in ITstudent_records:
                print("Record not found!")
                continue

    # Show existing data
            print("Current information:")
            for a in ITstudent_records[findthe_id]:
                print(f" >> {a}")

    # Ask for new values
            firstname = input("Type the NEW First Name: ").upper()
            lastname = input("Type the NEW Last Name: ").upper()
            year = input("Type the NEW Year: ").upper()
            email = input("Type the NEW Email: ").upper()
            status = input("Type the NEW Status: ").upper()
            age = input("Type the NEW Age: ").upper()
            home_address = input("Type the NEW Home address: ").upper()

    # Update the record
            ITstudent_records[findthe_id] = [
                firstname, lastname, year, email, status, age, home_address
            ]

            print(">>----------------The DATA has been UPDATED!---------------->> ")
            continue


    # EXPORT RECORD
        elif option == 'u':
            os.system('cls')
            print("Export IT Student Record File")
        #new file name, it is either read or write('r','w')

            with open("ITstudent_records.json","w") as new_file:
                json.dump(ITstudent_records , new_file, indent=4)
                print("------The DATA has been ExPORTED TO JSON-------")

            continue
        
        elif option == 't':
            os.system('cls')
            print("Import IT Student Record File")
            #new file name, it is either read or write('r','w')

            with open('ITstudent_records.json', 'r') as newfile:
                ITrecords_json = json.load(newfile)

            ITstudent_records = ITrecords_json
            print("<<-------The DATA has been IMPORTED TO JSON-------->>")

            continue
    # EXIT
        elif option == 's':
            print(">>--------------------------SYSTEM EXIT-----------------------------<<")
            break

        else:
            print("Invalid choice, please re-select your choice.")
            continue


#------------------------------------------------------------->> END OF CODE CHALLENGES <<--------------------------------------------------------------------------