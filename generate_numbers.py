def natural_numbers(n):
    return list(range(1, n + 1))
    #Returns a list of first 'n' natural numbers
    #Code here
    
def nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    #Returns n-th fibonacci number
    #Code here

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    #Return true if 'n' is prime, otherwise returns false
    #Code here