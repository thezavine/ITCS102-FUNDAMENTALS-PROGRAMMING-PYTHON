

#def artist(name):
#    print("WOAH! Can I have an autograph? ")

#artist("Kentorin")
#artist("Oda")
#artist("Futaba")

#Code Reusability

def artist(name):
    print(f"WOAH!{name}, Can I have an autograph? ")

def summation(a):
    sum = 0
    for b in range(a, 0, -1):
        sum += b
    print(f"The sum of {a} is {sum}")

summation(18)
summation(20)
