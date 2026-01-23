def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here