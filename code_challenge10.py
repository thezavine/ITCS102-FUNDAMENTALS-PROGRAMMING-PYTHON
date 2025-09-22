
print("\t\t\t   *",end=" ")
for a in range(1,15,1):
    for b in range(15, a, -1):
        print(" ", end=' ')
    for c in range(1, a, 1):
        print("*", end=' ')
    for d in range(1, a, 1):
        print("*", end=' ')
    print()