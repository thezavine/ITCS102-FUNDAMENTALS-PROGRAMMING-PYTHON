import os

os.system('cls')
print("IT students INFORMATION SYSTEM")
print(">>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<")

IT_records = {}

while True:
    print("Choose from the choices below\nz - Add Information\ny - Look for the information\nx- Remove the information\nw - Modify a information\nv - Saved Information\nu - EXIT")
    
    option = input("Your decision  >>>> ").lower()

    if option == "z":
        print("Combining IT Information")
        print("-------------------------------------------------")
        find_code = input("Key to find for the IT student: ")

        f_name = input("Type the IT student First Name: ").upper()
        l_name = input("Type the IT student Last Name: ").upper()
        year = input("Type the IT student year: ").upper()
        email = input("Type the IT Student Email address: ").upper()
        status = input("what is your status, right now? ").upper()
        age = input("How old are you? ").upper()
        home_address = input("Where do you live? ").upper()
        

        ITstudent_rec = {find_code : [f_name,l_name,year,email,status,age,home_address]}
        print("Information Saved")

        os.system('cls')
        continue

    elif option == "y":
        os.system('cls')
        code = input("Type the search code >> ")

        for a in ITstudent_rec.keys():
            if code in ITstudent_rec.keys():
                print("Record Located")

                print("Records ")
                print("==============")
                for b in ITstudent_rec[code]:
                    print(b)
                print("===============")

            else:
                print("No existing File")  
                continue
    elif option == "x":
        pass
        continue
    elif option == "w":
        print("Revising Record...")
        continue
    elif option == "v":
        for b,a in ITstudent_rec.items():
            print(f"CODE - {b} Archived Information >> {a}")
    elif option == "u":
        print("Program Termination")
        break
    else:
        print("Invalid OPTION, please RE-SELECT your option")
        continue
    