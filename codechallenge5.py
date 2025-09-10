#Create Manga Recommendation
#Options of Manga Recommendations
#Have fun reading

print("Welcome to the World of Manga  Selection: ")
print("Answer some of questions before we proceed on type of the manga's you want to know ")
print("What type of genre do you like? : ")

genre = int(input('\n1.Action\n2.Comedy\n3.Horror\nAnswer:'))

if genre ==  1:
    print("Welcome to the list of Action Manga Recommendations: ")

elif genre ==  2:
    print("Welcome to the list of Comedy Manga Recommendations: ") 

elif genre ==  3:
    print("Welcome to the list of Horror Manga Recommendation: ")

else:
    print("Sorry! We dont have that kind of Manga that you are looking here. Try another genre that we have here!")

print("How long the manga should be? ")

length = input("\n1.short\n2.medium\n3.long\nAnswer:")

if length == "1":
    print("You chose short now lets proceed on decade's")

elif length == "2":
    print("You chose medium now lets proceed on decade's")

elif length == "3":
    print("You chose long now lets proceed on decade's")

else:
    print("Sorry! We dont have that kind of choices here. Try again! ")

print("What decade's it should be? ")

year = input("\n1.1990s\n2.2000s\n3.2010s\nAnswer: ")

if year == "1":
	print("You chose 1990s,  Nice!")

elif year == "2":
	print("You chose 2000s,  Great for you!")

elif year == "3":
	print("You chose 2010s, Have fun!")

else:
	print("Sorry! We dont have that kind of choices here. Choose another one! ")


print("Here's some recommendation for you  for 2000s, 2015s, 2020s. Just look for them here : ")
year1  = input("Naruto (1999–2014) – Masashi Kishimoto \nBleach (2001–2016) –  One Piece (1997–present, huge in the 2000s) – Eiichiro Oda\nFullmetal\nAlchemist (2001–2010) – Hiromu Arakawa\nDeath Note (2003–2006) – Tsugumi Ohba & Takeshi Obata\nGantz (2000–2013) – Hiroya Oku\nD.Gray-man (2004–present) – Katsura Hoshino\nBlack Cat (2000–2004) – Kentaro Yabuki\nBuso Renkin (2003–2005) – Nobuhiro Watsuki\nEyeshield 21 (2002–2009) – Riichiro\nInagaki & Yusuke Murata")


