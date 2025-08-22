#comments
#jeepney fare
#user would input their name and section
#if user is pwd student, pwd student discount must be applied
#25% discount on pwd student, if pwd student, if not pwd student no discount

name =input("Input your name: --> ")
isPWDstudent = input("Are you a pwd student (Yes/No) --> ")
fare = eval(input("bayad -->  "))

if isPWDstudent == "yes":
	discount = fare *.25
	new_fare = fare - discount
	print("Hi", name, " pwd student discount is ", discount,
" Discouted fare is ", new_fare)
else: 
	print("Sorry", name," you are not eligible for pwd student discount")