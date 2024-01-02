import os, time

def factorial(value):
  if value == 1:
    return 1
  else: 
    return value * factorial(value - 1)

number = int(input("Enter the number : "))
result = factorial(number)
print(f"The factorial of {number} is {result}.")

while True:
  print()
  a = input("Again (y/n) : ").lower()
  if a == "y" or a == "yes":
    time.sleep(1)
    os.system("clear")
    number = int(input("Enter the number : "))
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
  else:
    break
