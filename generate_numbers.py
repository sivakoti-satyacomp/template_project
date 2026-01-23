def natural_numbers(n):
    return list(range(1, n+1))
    #Returns the list of natural numbers
    #Code here

def nth_fibonacci(n):
    a, b = 0, 1
    for meh in range(n):
        a, b = b, a + b
    return a
    #Returns n-th fibonacci number
    #Code here

def is_prime(n):
    if n <= 1:
        return False
    #Return true if 'n' is prime, otherwise returns false
    #Code here