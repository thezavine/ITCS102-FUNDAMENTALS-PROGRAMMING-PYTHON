



print("Adding Data to dictionary")
print(" <<<<<<<<<<<<<<<<<<< >>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
continously = True

void = {}

def print_manhwa():
    for c,d in void.items():
        print(f"CODE{c} >> TITLE << {d}")

while continously == True:
    keys = input("Enter the keys for this Manhwa ----> ")
    value = input("Enter any Manhwa title: ") 

    void[keys] = value

    option = input("Do you still wanna keep reading some Manhwa \nY - YEAH\nN - NOT AT ALL\nP - PRINT\n >>>...<<< ").lower()

    if option == 'y':
        print("Ongoing...")
        continue
    elif option == 'n':
        print("Program closes")
        break
    elif option == 'p':
        print_manhwa()
        continue
    else: 
        print("Error in selection")
        continue

    