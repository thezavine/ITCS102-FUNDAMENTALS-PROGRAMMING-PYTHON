from activity_menu import *
from codechallenge_menu import *

def my_project_header():
    print("\t------------------------------------------------------------------------>> <<------------------------------------------------------------------------------------")
    print("\t|\t\t\t\t\t\t\t\tPYTHON FINAL PROJECT\t\t\t\t\t\t\t\t\t\t|")
    print("\t------------------------------------------------------------------------>> <<------------------------------------------------------------------------------------")
    print("\t|\t\t\t\t\t\t\t>> Welcome to my Python Menu Program! <<\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\tAuthor: Azeth Arvine L. Brandes\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\tCourse: BSIT - 1A\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\tDescription:\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\tThis program is an interactive menu that showcases Python skills learned in\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\tthe Computer Programming subject. It contains:\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t1. A Python Starter Guide covering:\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\t- print, input, comments, variables, data types, operators\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\t- conditionals, loops, functions, lists, tuples, sets, dictionaries, symbols\t\t\t\t|")
    print("\t|\t\t\t\t\t\t2. Activity Files (1 - 28) demonstrating small projects and exercises\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t3. Code Challenges (1 - 16) for problem-solving practice\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\tHow to use:\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t1. Run the program.\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t2. Enter your name to begin.\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t3. Decide whether to proceed (y/n).\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t4. Use the main menu to choose:\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\tA - Starter Guide\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\tB - Activity Files\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\tC - Code Challenges\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\tD - Exit\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t5. Follow on-screen instructions for each section.\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\tNotes:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t- Input is case-insensitive.\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t- Activities and challenges must be selected by number.\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t- Exiting the program can be done from the main menu or at prompts.\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("\t|\t\t\t\t\tEnjoy exploring Python and learning step by step!\t\t\t\t\t\t\t\t\t|")
    print("\t------------------------------------------------------------------------>> <<------------------------------------------------------------------------------------")

# Call the function
my_project_header()

# >>--------------------------------------------------------------------- STARTER GUIDE MENU ----------------------------------------------------------------------- <<
name = input("\n\t\t\t\t\t\t\t\tHello, May I know your name? ")
print(f"\t\t\t\t\t\t\tGreetings {name}, Let me introduce myself to you. ")
print("\t\t>>>-----------------------------------------------------------------------------------------------------------------------------------------------<<<")
print("\t\t>>\t\t\t\t\t KONNICHIWA! Again, I am Azeth Arvine L. Brandes from BSIT - 1A \t\t\t\t\t   <<")
print("\t\t>>\t\t\t\t\t\t WELCOME TO MY PYTHON MENU ₊˚⊹ ᰔ \t\t\t\t\t\t\t\t   << ")
print("\t\t>> All of my activities from 1 - 28 and code challenges from 1 - 16 are here to let you see what I had learn from our SUBJECT COMPUTER PRGOGRAMMING<< ")
print("\t\t>>\t\t\t\t\t I HOPE YOU ENJOY CODING AND TRYING MY MENU \t\t\t\t\t\t\t\t   <<")
print("\t\t>>>-----------------------------------------------------------------------------------------------------------------------------------------------<<<")

choice = input("\t\t\t\t\t\tDo you still want to proceed? (y/n): ").lower()

if choice == "y":
    print("\t\t\t\t\tProceeding...")

elif choice == "n":
    print("\t\t\t\t\tOperation cancelled.")
    exit()

else:
    print("Invalid input.")
    exit()

# >>--------------------------------------------------------<<
# |   STARTER GUIDE FUNCTIONS (DEFINITION + EXAMPLES)        |
# >>--------------------------------------------------------<<

# -------------------- PRINT (A) --------------------
def print_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tPRINT STATEMENT - DEFINITION\t\t|")
    print("--------------------->>  <<----------------------\n")
    print("The print() function displays messages, numbers, variables, or results on the screen.")
    print("It is the primary way to output information in Python.\n")
    print("It supports parameters like 'sep' and 'end' that control formatting.\n")
    print("----------->>End of Print Definition<<---------------\n")

def print_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tPRINT STATEMENT - EXAMPLES\t\t|")
    print("--------------------->>  <<----------------------\n")
    print("Example 1: Printing text directly")
    print("Hello, World!\n")
    print("Example 2: Printing numeric values")
    print(123)
    print(3.14, "\n")
    print("Example 3: Printing multiple values together")
    name = 'Azeth Arvine Brandes'
    age = 20
    print('Name:', name, 'Age:', age, '\n')
    print("Example 4: Using f-strings")
    print(f"My name is {name} and I am {age} years old.\n")
    print("Example 5: Printing multiple lines using \\n")
    print("Line 1\nLine 2\nLine 3\n")
    print("----------->>End of Print Examples<<---------------\n")

# -------------------- INPUT (B) --------------------
def input_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tINPUT STATEMENT - DEFINITION\t\t|")
    print("--------------------->>  <<----------------------\n")
    print("The input() function allows users to enter information during execution.")
    print("All input is captured as text (string) by default.\n")
    print("----------->>End of Input Definition<<---------------\n")

def input_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tINPUT STATEMENT - EXAMPLES\t\t|")
    print("--------------------->>  <<----------------------\n")
    print("Example 1:")
    print("user_name = input('Enter your name: ')")
    print("print('Hello, ' + user_name + '!')\n")
    print("Example 2:")
    print("age_input = int(input('Enter your age: '))")
    print("print('You are', age_input, 'years old.')\n")
    print("----------->>End of Input Examples<<---------------\n")

# -------------------- COMMENTS (C) --------------------
def comments_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tCOMMENTS - DEFINITION\t\t|")
    print("--------------------->>  <<----------------------\n")
    print("Comments are explanatory notes ignored by Python.")
    print("They help make code readable.\n")
    print("----------->>End of Comments Definition<<---------------\n")

def comments_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tCOMMENTS - EXAMPLES\t\t|")
    print("--------------------->>  <<----------------------\n")
    print("Single-line comment:")
    print("# This is a comment\n")
    print("Multi-line comment:")
    print('''"""
This is a
multi-line comment
used for detailed explanations
"""''')
    print("\n----------->>End of Comments Examples<<---------------\n")

# -------------------- VARIABLES (D) --------------------
def variables_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tVARIABLES - DEFINITION\t\t|")
    print("--------------------->>  <<----------------------\n")
    print("Variables store data values that may change.")
    print("Python supports int, float, str, bool, list, tuple, set, dict.\n")
    print("----------->>End of Variables Definition<<---------------\n")

def variables_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tVARIABLES - EXAMPLES\t\t|")
    print("--------------------->>  <<----------------------\n")
    name = "Azeth Arvine Brandes"
    age = 20
    is_student = True
    print(f"name = '{name}'")
    print(f"age = {age}")
    print(f"is_student = {is_student}\n")
    print("Updated age example:")
    age = 21
    print(f"Updated age = {age}\n")
    print("----------->>End of Variables Examples<<---------------\n")

# -------------------- OPERATORS (E) --------------------
def operators_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tOPERATORS - DEFINITION\t\t|")
    print("--------------------->>  <<----------------------\n")
    print("Operators perform operations on variables and values.")
    print("Includes arithmetic, comparison, logical, assignment operators.\n")
    print("----------->>End of Operators Definition<<---------------\n")

def operators_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tOPERATORS - EXAMPLES\t\t|")
    print("--------------------->>  <<----------------------\n")
    a = 10
    b = 3
    print("Arithmetic:")
    print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
    print("\nComparison:")
    print(a == b, a != b, a > b)
    print("\nLogical:")
    print(True and False)
    print("----------->>End of Operators Examples<<---------------\n")

# -------------------- CONDITIONALSE (F) --------------------
def cond_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tCONDITIONALS - DEFINITION\t|")
    print("--------------------->>  <<----------------------\n")
    print("Conditionals allow branching using if, elif, else.\n")
    print("----------->>End of Conditional Definition<<---------------\n")

def cond_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tCONDITIONALS - EXAMPLES\t|")
    print("--------------------->>  <<----------------------\n")
    x = 10
    if x > 15:
        print("x > 15")
    elif x > 5:
        print("x > 5 but ≤ 15")
    else:
        print("x ≤ 5")
    print("\n----------->>End of Conditional Examples<<---------------\n")

# -------------------- LOOPS (G) --------------------
def loops_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tLOOPS - DEFINITION\t\t|")
    print("--------------------->>  <<----------------------\n")
    print("Loops repeat code using for or while.\n")
    print("----------->>End of Loops Definition<<---------------\n")

def loops_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tLOOPS - EXAMPLES\t\t|")
    print("--------------------->>  <<----------------------\n")
    print("For loop 1–5:")
    for i in range(1, 6):
        print(i)
    print("\nWhile loop:")
    n = 5
    while n > 0:
        print(n)
        n -= 1
    print("\n----------->>End of Loops Examples<<---------------\n")

# -------------------- FUNCTIONS (H) --------------------
def func_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tFUNCTIONS - DEFINITION\t|")
    print("--------------------->>  <<----------------------\n")
    print("Functions are reusable blocks of code.\n")
    print("----------->>End of Functions Definition<<---------------\n")

def func_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tFUNCTIONS - EXAMPLES\t|")
    print("--------------------->>  <<----------------------\n")
    def greet(name):
        print(f"Hello, {name}!")
    greet("Azeth Arvine Brandes")
    print("\n----------->>End of Functions Examples<<---------------\n")

# -------------------- LISTS (I) --------------------
def list_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tLISTS - DEFINITION\t|")
    print("--------------------->>  <<----------------------\n")
    print("Lists store multiple ordered, changeable items.\n")
    print("----------->>End of Lists Definition<<---------------\n")

def list_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tLISTS - EXAMPLES\t|")
    print("--------------------->>  <<----------------------\n")
    fruits = ["pineapple", "kiat-kiat", "dragonfruit"]
    print(fruits)
    fruits.append("kiwi")
    print(fruits)
    print("\n----------->>End of Lists Examples<<---------------\n")

# -------------------- TUPLES (J) --------------------
def tuple_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tTUPLES - DEFINITION\t|")
    print("--------------------->>  <<----------------------\n")
    print("Tuples are like lists but immutable.\n")
    print("----------->>End of Tuples Definition<<---------------\n")

def tuple_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tTUPLES - EXAMPLES\t|")
    print("--------------------->>  <<----------------------\n")
    coordinates = (10, 20)
    print(coordinates)
    print("\n----------->>End of Tuples Examples<<---------------\n")

# -------------------- SETS (K) --------------------
def set_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tSETS - DEFINITION\t|")
    print("--------------------->>  <<----------------------\n")
    print("Sets store unique, unordered items.\n")
    print("----------->>End of Sets Definition<<---------------\n")

def set_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tSETS - EXAMPLES\t|")
    print("--------------------->>  <<----------------------\n")
    my_set = {1, 2, 3}
    print(my_set)
    my_set.add(4)
    print(my_set)
    my_set.add(2)
    print(my_set)
    print("\n----------->>End of Sets Examples<<---------------\n")

# -------------------- DICTIONARY (L) --------------------
def dict_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tDICTIONARY - DEFINITION\t|")
    print("--------------------->>  <<----------------------\n")
    print("Dictionaries store key-value pairs.\n")
    print("----------->>End of Dictionary Definition<<---------------\n")

def dict_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\t\tDICTIONARY - EXAMPLES|")
    print("--------------------->>  <<----------------------\n")
    person = {"name": "Azeth Arvine Brandes", "age": 20}
    print(person)
    person["city"] = "Paris"
    print(person)
    print("\n----------->>End of Dictionary Examples<<---------------\n")

# -------------------- SYMBOLS (M) --------------------
def symbols_def():
    print("\n--------------------->>  <<----------------------")
    print("|\tSYMBOLS - DEFINITION\t|")
    print("--------------------->>  <<----------------------\n")
    print("Python syntax uses symbols like (), {}, [], :, , and =.\n")
    print("----------->>End of Symbols Definition<<---------------\n")

def symbols_ex():
    print("\n--------------------->>  <<----------------------")
    print("|\tSYMBOLS - EXAMPLES\t|")
    print("--------------------->>  <<----------------------\n")
    print("Examples of symbols used in Python were shown earlier in your content.\n")
    print("----------->>End of Symbols Examples<<---------------\n")

# >>--------------------------------------------------------<<
# |      MAIN MENU + STARTER GUIDE SUBMENU WITH DEF/         |
# >>--------------------------------------------------------<<
while True:
    print("\n\t\t\t\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\t\t\t\t>>\t------->> PLEASE SELECT from the CHOICES BELOW the PYTHON that you want to LEARN <<------\t<<")
    print("\t\t\t\t>>\t\t\t\t A - STARTER GUIDE\t\t\t\t\t\t\t<<")
    print("\t\t\t\t>>\t\t\t\t B - ACTIVITY FILES (1 - 28)\t\t\t\t\t\t<<")
    print("\t\t\t\t>>\t\t\t\t C - CODE CHALLENGES (1 - 16)\t\t\t\t\t\t<<")
    print("\t\t\t\t>>\t\t\t\t D -    EXIT   \t\t\t\t\t\t\t\t<<")
    print("\t\t\t\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    option = input("\t\t\t\t\tYour decision ------> ").lower()


    if option == 'a':
        while True:
            print("\n-------------------->>  <<------------------------")
            print("|\t\tPYTHON STARTER GUIDE\t\t |")
            print("-------------------->>  <<------------------------")

            print("|\tPlease choose from the choices below:\t |")
            print("|\ta.) Print Statement\t\t\t |")
            print("|\tb.) Input Statement\t\t\t |")
            print("|\tc.) Comments\t\t\t\t |")
            print("|\td.) Variables and Data Types\t\t |")
            print("|\te.) Operators\t\t\t\t |")
            print("|\tf.) Conditionals\t\t\t |")
            print("|\tg.) Loops\t\t\t\t |")
            print("|\th.) Functions\t\t\t\t |")
            print("|\ti.) Lists\t\t\t\t |")
            print("|\tj.) Tuples\t\t\t\t |")
            print("|\tk.) Sets\t\t\t\t |")
            print("|\tl.) Dictionaries\t\t\t |")
            print("|\tm.) Symbols\t\t\t\t |")
            print("|\tq.) Quit\t\t\t\t |")
            print("--------------------------------------------------")

            topic = input("\t Enter your selection...\t\t-----> ").lower()

        # ---------- DEFINITION / EXAMPLES SUBMENU ----------
            def def_ex_menu(def_func, ex_func):
                while True:
                    print("  ----------------->>  <<----------------")
                    print("  |\tChoose from the choices below:\t|")
                    print("  ----------------->>  <<----------------")
                    print("  |\t\t1 - Definition\t\t|")
                    print("  |\t\t2 - Examples\t\t|")
                    print("  |\t\t3 - Back\t\t|")
                    print("  ---------------------------------------")


                    choice = input("\t Your decision... \t\t\t----> ")


                    if choice == "1":
                        def_func()
                    elif choice == "2":
                        ex_func()
                    elif choice == "3":
                        break
                    else:
                        print("\tInvalid choice!")

            if topic == 'a': 
                def_ex_menu(print_def, print_ex)
            elif topic == 'b': 
                def_ex_menu(input_def, input_ex)
            elif topic == 'c': 
                def_ex_menu(comments_def, comments_ex)
            elif topic == 'd': 
                def_ex_menu(variables_def, variables_ex)
            elif topic == 'e': 
                def_ex_menu(operators_def, operators_ex)
            elif topic == 'f': 
                def_ex_menu(cond_def, cond_ex)
            elif topic == 'g': 
                def_ex_menu(loops_def, loops_ex)
            elif topic == 'h': 
                def_ex_menu(func_def, func_ex)
            elif topic == 'i': 
                def_ex_menu(list_def, list_ex)
            elif topic == 'j': 
                def_ex_menu(tuple_def, tuple_ex)
            elif topic == 'k': 
                def_ex_menu(set_def, set_ex)
            elif topic == 'l': 
                def_ex_menu(dict_def, dict_ex)
            elif topic == 'm': 
                def_ex_menu(symbols_def, symbols_ex)
            elif topic == 'q':
                print("\tLeaving Starter Guide...")
                break

            else:
                print("\tInvalid option.")

    # -------------------------------------------------------------------- << ACTIVITY MENU >> ------------------------------------------------------------------------
    elif option == 'b':
        print("\n\t\t\t\t\t-------------------------------->> SELECT Activity Number (1 - 28) <<----------------------------------------")
        print(" 1  - FIRST PROGRAM / PRINTING TEXT (ACTIVITY 1)")
        print(" 2  - PRINT USING COMMAS (ACTIVITY 2)")
        print(" 3  - PRINT USING TABS AND NEW LINES (ACTIVITY 3)")
        print(" 4  - STRING LENGTH USING LEN() (ACTIVITY 4)")
        print(" 5  - DETECT DATA TYPE USING EVAL() (ACTIVITY 5)")   
        print(" 6  - ARITHMETIC OPERATORS (ACTIVITY 6)")
        print(" 7  - ASSIGNMENT OPERATORS (ACTIVITY 7)")
        print(" 8  - RELATIONAL OPERATORS (ACTIVITY 8)")
        print(" 9  - LOGICAL OPERATORS (ACTIVITY 9)")       
        print(" 10 - IF/ELSE STATEMENT SELECTION (ACTIVITY 10)")
        print(" 11 - TEMPERATURE INSPECTOR (ACTIVITY 11)")
        print(" 12 - PRINT HELLO WORLD USING FOR LOOP (ACTIVITY 12)")
        print(" 13 - SUMMATION USING FOR LOOP (ACTIVITY 13)")
        print(" 14 - COUNTING IN REVERSE USING FOR LOOP (ACTIVITY 14)")
        print(" 15 - STRING FORMATTING AND TABLES (ACTIVITY 15)")
        print(" 16 - PRINT NUMBERS IN A NEW LINE (ACTIVITY 16)")
        print(" 17 - NESTED FOR LOOP DEMONSTRATION (ACTIVITY 17)")
        print(" 18 - ITERATION OUTPUT OF NESTED LOOPS (ACTIVITY 18)")
        print(" 19 - RIGHT TRIANGLE STAR PATTERN (ACTIVITY 19)")
        print(" 20 - INVERTED RIGHT TRIANGLE STAR PATTERN (ACTIVITY 20)")
        print(" 21 - LIBRARY ARRANGEMENT LOOP (ACTIVITY 21)")
        print(" 22 - GUESS THE NUMBER GAME USING RANDOM (ACTIVITY 22)")
        print(" 23 - LIST SLICING AND REVERSING (ACTIVITY 23)")
        print(" 24 - SUMMATION FUNCTION (ACTIVITY 24)")
        print(" 25 - MENU OPTIONS / SUM ODD NUMBERS / FACTORIAL / TRIANGLE (ACTIVITY 25)")
        print(" 26 - DICTIONARY DEMONSTRATION (ACTIVITY 26)")
        print(" 27 - ADDING DATA TO DICTIONARY (ACTIVITY 27)")
        print(" 28 - SNAKE GAME USING PYGAME (ACTIVITY 28)")


        act = input("\t\t\t\t\t>>\t Choose Activity Number:")
    


        if act == "1":
            activity1()
        elif act == "2":
            activity2()
        elif act == "3":
            activity3()
        elif act == "4":
            activity4()
        elif act == "5":
            activity5()
        elif act == "6":
            activity6()
        elif act == "7":
            activity7()
        elif act == "8":
            activity8()
        elif act == "9":
            activity9()
        elif act == "10":
            activity10()
        elif act == "11":
            activity11()
        elif act == "12":
            activity12()
        elif act == "13":
            activity13()
        elif act == "14":
            activity14()
        elif act == "15":
            activity15()
        elif act == "16":
            activity16()
        elif act == "17":
            activity17()
        elif act == "18":
            activity18()
        elif act == "19":
            activity19()
        elif act == "20":
            activity20()
        elif act == "21":
            activity21()
        elif act == "22":
            activity22()
        elif act == "23":
            activity23()
        elif act == "24":
            activity24()
        elif act == "25":
            activity25()
        elif act == "26":
            activity26()
        elif act == "27":
            activity27()
        elif act == "28":
            activity28()

        else:
            print("Activity not found or not yet added!")

    # -------------------------------------------------------------------------- << CODE CHALLENGE MENU >> -------------------------------------------------------------
    elif option == 'c':
        while True:
            print("\n------------------------------------------------------->> SELECT Code Challenge Number (1 - 16) <<------------------------------------------------------")
            print(". \t1 - NAME INSIDE OF PYRAMID(CODE CHALLENGE 1) \t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t2 - AMOUNT DEPOSIT(CODE CHALLENGE 2) \t\t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t3 - IF, ELSE USERNAME AND PASSWORD(CODE CHALLENGE 3) \t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t4 - IDENTIFYING ODD OR EVEN(CODE CHALLENGE 4) \t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t5 - MANGA RECOMMENDATION(CODE CHALLENGE 5) \t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t6 - FACTORIAL PROGRAM(CODE CHALLENGE 6) \t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t7 - ODD NUMBER SUMMATION(CODE CHALLENGE 7) \t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t8 - MULTIPLICATION TABLE MAKER(CODE CHALLENGE 8)\t\t\t\t\t\t\t\t\t\t\t\t. ")
            print(". \t9 - COUNTDOWN TIMER STIMULATOR(CODE CHALLENGE 9) \t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t10 - TRIANGLE FOR LOOP(CODE CHALLENGE 10)\t\t\t\t\t\t\t\t\t\t\t\t\t. ")
            print(". \t11 - DIAMOND USING FOR LOOP(CODE CHALLENGE 11) \t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t12 - NUMBER TRIANGLE USING FOR LOOP(CODE CHALLENGE 12)\t\t\t\t\t\t\t\t\t\t\t\t. ")
            print(". \t13 - CHRISTMAS TREE(CODE CHALLENGE 13) \t\t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t14 - ODD NUMBERS DETECTOR(CODE CHALLENGE 14) \t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t15 - ANIME WATCHLISTS(CODE CHALLENGE 15) \t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \t16 - IT STUDENT INFORMATION SYSTEM(CODE CHALLENGE 16) \t\t\t\t\t\t\t\t\t\t\t\t.")
            print(". \tE - Exit to Main Menu\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t.")
            print("-------------------------------------------------------------------->><<---------------------------------------------------------------------------------")


            code_challenge = input("\tChoose Code Challenge number\t\t\t\t--->>")


            if code_challenge == "1":
                codechallenge1()
            elif code_challenge == "2":
                codechallenge2()
            elif code_challenge == "3":
                codechallenge3()
            elif code_challenge == "4":
                codechallenge4()
            elif code_challenge == "5":
                codechallenge5()
            elif code_challenge == "6":
                codechallenge6()
            elif code_challenge == "7":
                codechallenge7()
            elif code_challenge == "8":
                codechallenge8()
            elif code_challenge == "9":
                codechallenge9()
            elif code_challenge == "10":
                codechallenge10()
            elif code_challenge == "11":
                codechallenge11()
            elif code_challenge == "12":
                codechallenge12()
            elif code_challenge == "13":
                codechallenge13()
            elif code_challenge == "14":
                codechallenge14()
            elif code_challenge == "15":
                codechallenge15()
            elif code_challenge == "16":
                codechallenge16()
            elif code_challenge == "e":
                print("Returning to MAIN MENU...")
                break

            else:
                print("Code Challenge not found or not yet added!")

    # ------------------------------- << EXIT >> ----------------------------------------
    
    elif option == 'd':
        print("\nThank you for using the program! Goodbye ₊˚⊹ ᰔ")
        break

    else:
        print("\nInvalid option! Please choose A, B, or C.")

#---------------------------------------------------------------------------- >> THE END << ------------------------------------------------------------------------