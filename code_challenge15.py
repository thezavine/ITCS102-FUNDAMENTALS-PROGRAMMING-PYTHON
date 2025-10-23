#Anime to watch lists
#Use a while loop and list
print("List of Anime Titles")

anime = [] 
manga = True   

while manga == True:
    num = input("Enter the title of an Anime: ")
    print(f"'{num}' has been added to your Anime List")
    anime.append(num) #all title that you had enter will go to the list
    if num == "exit": #it stops when you put the 'exit' word
        print("Well done! The anime entry program has exited successfully!! ")
        anime.pop() 
        break   

print(f"Here are your anime titles: ") 
for r in anime:     
    print(f"- {r}")