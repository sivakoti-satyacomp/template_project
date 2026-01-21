def natural_numbers(n):
    #Returns the list of natural numbers
    return list(range(1, n + 1))

def nth_fibonacci(n):
    #Returns n-th fibonacci number
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True
