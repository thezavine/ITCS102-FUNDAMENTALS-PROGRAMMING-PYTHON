

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
