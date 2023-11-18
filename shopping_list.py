shopping_list = []
x = int(input("How many items would you like to add :"))
for number in range(x):
  shopping_list.append(input("What item would you like to add: "))
  print("So your cart is: ", shopping_list)
  if x == 0:
    print("I see you do not want anything") 
