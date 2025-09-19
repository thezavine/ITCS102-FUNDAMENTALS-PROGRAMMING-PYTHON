#STRING FORMATTING
#FULLNAME, AGE, CURRENT ADDRESS

full_name = 'Azeth Arvine L. Brandes'
age = '20'
cu_add = 'Barangay 8, Lagos Street, Lucena City'

#print(f"My full name is {full_name}. I am {age} yrs old and I live in {cu_add}")

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


