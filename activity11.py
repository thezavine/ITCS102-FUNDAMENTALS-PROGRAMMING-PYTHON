#create a program that accepts float values
#determine temperature weather reading
#1 to 19 is cold
#20 to 30 is lukewarm
#31 to 45 is warm
#46 to 50 is hot 
#51 and above is super hot

temp = eval(input("Enter temperature --> "))

if temp >= 1 and temp <= 19:
	print("temperature outside is cold")
elif temp >= 20 and temp <= 30:
	print("temperature outside is lukewarm")
elif temp >= 31 and temp <= 45:
	print("temperature outside is warm")
elif temp >= 46 and temp <= 50:
	print("temperature outside is hot")
elif temp >= 51:
	print("temperature outside is super hot")


else:
	print("invalid temperature")