def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    return [i for i in range(1,n+1)]

def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a if n > 0 else 0

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True