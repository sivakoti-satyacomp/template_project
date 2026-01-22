import math
def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    return list(range(1, n+1))
print(natural_numbers(10))


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    if n == 0:
        return 0
    if n == 1:
        return 1
    a , b = 0, 1
    for i in range(2, n+1):
        a , b = b, a+b
    return b
print(nth_fibonacci(7))

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    if (n <= 1):
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if (n % i == 0):
            return False
    return True
print(is_prime(24))