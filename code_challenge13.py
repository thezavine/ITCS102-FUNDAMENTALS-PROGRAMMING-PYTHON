#Christmas Tree

for i in range(1, 3, 1):
    for b in range(10, i, -1):
        print(i, end= " ")
    for layer in range(0,i,1):
        print(" ",end=' ')
    for i in range(1,3,1):
       print(" ",end= "|_|")
for j in range(1, 3, 2):
    for k in range(i, 0, -2):
        print(i, end= " ")
    for layer in range(1,3,1):
       for i in range(1, 2 + 1):
           print(" ",end=' ')
    for l in range(1,3,1):
       print(" ",end="|_|")
    print(i)
