all_pokemon = []
x = int(input("How many pokemon would you like to add: "))
for number in range (x):
  pokemon = []
  all_pokemon.append(pokemon)

 
  pokemon.append(input("What is its name: "))
  pokemon.append(input("What is its typing: "))
  pokemon.append(int(input("What is its base hp stat: ")))
  if number != x-1:
    print("Now please fill out the information on the next pokemon")


# [['d', 'a', 1], ['a', 'd', 1], ['d', 'a', 1]]
for p in all_pokemon:
 print("\n" *5)
 print("This Pokemon is called " + str(p[0]))
 print("and is a " + str(p[1]) + " type")
 print("its hp stat is also " + str(p[2]))

  

# [["name", "type", 150], ["name", "type", 150], ["name", "type", 150]]




