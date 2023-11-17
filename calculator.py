n1 = int(input("Please enter your first number "))  

operation = input("Please enter the operation you are willing to use ")
while operation != "+" and operation != '-' and operation != "/" and operation != "*" and operation != "x":
  operation = input("Invalid operation please enter it again ")

n2 = int(input("Please enter your second number "))

if operation == "+":
  j = n1 + n2
elif operation == "-":
  j = n1 - n2
elif operation == "/":
  j = n1 / n2
elif operation == "*":
  j = n1 * n2
elif operation == "x":
  j = n1 * n2 
print(round(j, 1))
