import random

a = input("Do you want to play easy, medium or hard mode? ")
if a == "easy":
  x = random.randint(1, 10000)
elif a == "medium":
  x = random.randint(1, 10000000)
elif a.lower() == "hard":
  x = random.randint(1, 100000000000000)
else:
  print("Don't waste my time put an actual gameode on I'm going to make you restart the code now")
  quit()

print(x)
input("Press enter when you are ready")
print("\n" * 100)
y = int(input("Place your guess: "))
if x != y:
  print("Incorrect it was ")
  print(x)
else:
  print("Correct!")
