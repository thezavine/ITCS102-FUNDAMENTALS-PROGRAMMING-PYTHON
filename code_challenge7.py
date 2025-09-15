#code challenge
#Odd number summation

print("ODD NUMBER SUMMATION")

result = 0
for x in range(10):
        num = eval(input("Enter a number:  "))
        if num % 2 != 0:
            result += num

print("The sum of all the ODD numbers is ",result)
