
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def summation():
  sum = 0
  for n in range(11):
    #print(n)  
    sum += 1 / factorial(n)
  return sum
print("The ans is:"+str(summation()))


