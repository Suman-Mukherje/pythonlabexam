

def find_divisors(number):
  divisors = []
  for i in range(1, number + 1):
    if number % i == 0:
      divisors.append(i)
  return divisors


number = int(input("Enter a number: "))
divisors = find_divisors(number)
print("The divisors of {} are: {}".format(number, divisors))


