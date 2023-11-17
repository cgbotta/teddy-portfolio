import random

x = random.randint(1, 10)
y = int(input("What is your guess: "))
while y != x:
  if y < x:
    y = int(input("Your guess is too small - try again: "))
  else:
    y = int(input("Your guess is too big - try again: "))
print("Correct!")
