

year = ['2001','2002','2003','2004','2005','2006']

#functions
#year.append('2005')
#print(year)
#year.pop()
#print(year)
#year.append('2006')
#print(year)

#Iteration/Traversing a List
for y in year:
    print(f"{y}, December")

birthdate = 'December 27, 2004'

#List Slicing

#for b in birthdate:
#    print(b)

#for b in birthdate[-1:0]:
#    print(b)

another = list(birthdate)

another.reverse()

print(another)

