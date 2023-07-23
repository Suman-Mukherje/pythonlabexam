
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

number = int(input("Enter a number: "))
print("The factorial of given number is: "+str(factorial(number)))


