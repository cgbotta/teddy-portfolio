# Background and comcepts
my_list = [1, 25, 3, 10, 5]
print(my_list)
print(my_list[0])

my_list[0]=100
print(my_list)


my_list = [1, 25, 3, 10, 5]
for x in my_list:
  print(x+10) 


for x in reversed(my_list):
  print(x)

# range(5) = [0,1,2,3,4]
for number in range(3, 71):
  print(number)
  
my_list = [1, 25, 3, 10, 5, 50, 2]
my_list.append(50)  #append always adds to the end
print(my_list)

my_list = [70, 1, 25, 3, 10, 5, 50, 2]
my_list.insert(0, 70) #if we want to add anywhere else, use insert and tell it what index to add at
print(my_list)

w = [1, 2, 3, 'w', [29, 30, [19]], 4]
print(w[4][2])



Shopping List Program
shopping_list = []
x = int(input("How many items would you like to add :"))
for number in range(x):
  shopping_list.append(input("What item would you like to add: "))
  print("So your cart is: ", shopping_list)
if x == 0:
  print("I see you do not want anything")


Pokemon List Program
print("Lets add some pokemon \n")
x = 1
all_pokemon = []
while x < 2:
  c = input("\nWhat is its name : ")
  pokemon = []
  pokemon.append(c)
  pokemon.append(input("\nWhat is its typing: "))
  pokemon.append(int(input("\nWhat is its base hp stat: ")))
  # loop through all_pokemon
  #Check if we already have the name = c in our list
  # if we don't have it, append our pokemon to the list
  Found = False
  for p in all_pokemon:
    if c == p[0]:
      Found = True
      print("\nPokemon is already in the list")
  if Found == False:   
   all_pokemon.append(pokemon)
   y = input("\nType \"1\" if you are finished: ")
  if y == "1":
   x = x + 3
  else:
     print("\nNow please fill out the information on the next pokemon")

j = 2
while j == 2:
  a = input("\nWhich pokemon would you like to look for: ")
  found = False
  for p in all_pokemon:
    if a == p[0]:
      print("\nThis Pokemon is called " + str(p[0]))
      print("and is a " + str(p[1]) + " type")
      print("its hp stat is also " + str(p[2]))
      found = True

  if found == False:
    print("\nThe pokemon is not in the list")
  b = input("\nis that all? Type \"y\" for yes: ")
  

  if b == "y":
    j=j+1
    
      
     
     
     
     
    all_pokemon = [["name", "type", 150], ["name", "type", 150], ["name", "type", 150]]
     p = ["name", "type", 150]
    a = name




import csv

file = open("pokemon.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()

pokedex_number = input("Please enter the pokedex number of your pokemon: ")
for p in data:
  if p[0] == pokedex_number:
    print(p)
