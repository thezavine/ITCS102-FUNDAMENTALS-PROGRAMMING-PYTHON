#FACTORIAL PROGRAM
#The factorial of 5! is 120

print("FACTORIAL PROGRAM")

num = eval(input("Input a number -->   "))

result = 1
for x in range(num, 0, -1):
    print(result, "*", x, "=", result * x )
    result *= x

print("Factorial is ", result)
