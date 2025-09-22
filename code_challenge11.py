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
for d in range(9,0,-1):
    for e in range(10,d,-1):
        print(" ",end=" ") 
    for f in range(0,d,1):
        print("*",end=" ") 
    for g in range(1,d,1):
        print("*",end=" ")
    for h in range(10,d,-1):
        print(" ",end=" ")
    print()