#Christmas TREE


for a in range(1,3,1):         #Diamond
    for b in range(11,a,-1):
        print(" ",end=" ") 
    for c in range(0,a,1):
        print(".",end=" ") 
    for d in range(1,a,1):
        print(".",end=" ")
    for e in range(0,a,-1):
        print(" ",end=" ")
    print()
for f in range(3,0,-1):         #First TRIANGLE
    for g in range(11,f,-1):
        print(" ",end=" ") 
    for h in range(0,f,1):
        print(".",end=" ")
    for i in range(1,f,1):
        print(".",end=" ")
    for j in range(1,12,1):
        print(" ",end=" ")
    print()
for w in range(1,12,1):     #Second TRIANGLE
    for l in range(11,w,-1):
        print(" ",end=" ") 
    for m in range(0,w,1):
        print("-",end=" ") 
    for n in range(1,w,1):
        print("-",end=" ")
    for o in range(12,w,1):
        print(" ",end=" ")
    print()
for v in range(1,12,1):     #Third part of the TRIANGLE
    for o in range(11,v,-1):
        print(" ",end=" ") 
    for p in range(0,v,1):
        print("-",end=" ") 
    for q in range(1,v,1):
        print("-",end=" ")
    for r in range(12,v,1):
        print(" ",end=" ")
    print()
for u in range(1,8,1):
    for s in range(8,0,-1):
        print(" ",end=" ") 
    for t in range(5, 0 ,-1):
        print("|",end=" ") 
    print()
