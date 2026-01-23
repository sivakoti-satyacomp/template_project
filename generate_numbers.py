def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True