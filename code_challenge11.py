#Make a diamond using for loop


for a in range(1,11,1):
    for b in range(10,a,-1):  
        print(" ",end=" ") 
    for c in range(0,a,1):
        print("*",end=" ") 
    for d in range(1,a,1):
        print("*",end=" ")
    for e in range(10,a,-1):
        print(" ",end=" ")
    print()



#Then make the reverse triangle
for f in range(9,0,-1):
    for g in range(10,f,-1):
        print(" ",end=" ") 
    for g in range(0, f, 1):
        print("*",end=" ") 
    for i in range(1, f, 1):
        print("*",end=" ")
    for j in range(10, f, -1):
        print(" ",end=" ")
    print()