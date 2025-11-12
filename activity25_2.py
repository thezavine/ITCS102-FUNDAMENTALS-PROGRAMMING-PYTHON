def factorial(num):
    facto = 1
    for b in range(num, 0, -1):
        facto *= b
    return facto

def some_triangle(num):
    for i in range(1, num + 1):
        print("* " * i)
