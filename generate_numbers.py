def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here

def is_prime(n):
    if n < 2:
        return False
    # Only need to check up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True