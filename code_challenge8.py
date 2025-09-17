#Print a number entered by the user, using a simple for loop.
#Multiplication table

print("MULTIPLICATION TABLE MAKER")

# Ask the user to enter a number
num = eval(input("Enter a number: "))

print("\nMultiplication table for",num, ":")
#it doesn't need to put the "result" or add another variable
#it only needs the multiplication table

for x in range(1, 11):
    print(num, "x", x, "=", num * x)
