
def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True


number = int(input("Enter a number: "))
primes = []
if (number == 1):
    print("1 is not prime no so it's not possible to return a list")
else:
    for i in range(2, number + 1):
        if is_prime(i):
            primes.append(i)
    print("The prime numbers upto given number is: "+str(primes))


