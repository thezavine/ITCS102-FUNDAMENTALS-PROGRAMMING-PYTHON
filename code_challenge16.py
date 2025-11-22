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
        for a in ITstudent_records[findthe_id]:
                    print(f" >> {a}")

        firstname = input("Type the NEW First Name: ").upper()
        lastname = input("Type the NEW Last Name: ").upper()
        year = input("Type the NEW Year: ").upper()
        email = input("Type the NEW Email: ").upper()
        status = input("Type the NEW Status: ").upper()
        age = input("Type the NEW Age: ").upper()
        home_address = input("Type the NEW Home address: ")

        ITstudent_records[findthe_id][0] = firstname
        ITstudent_records[findthe_id][1] = lastname
        ITstudent_records[findthe_id][2] = year
        ITstudent_records[findthe_id][3] = email
        ITstudent_records[findthe_id][4] = status
        ITstudent_records[findthe_id][5] = age
        ITstudent_records[findthe_id][6] = home_address

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
