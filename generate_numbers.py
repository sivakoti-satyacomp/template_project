def natural_numbers(n):
    # Returns the list of natural numbers
    return list(range(1, n + 1))


def nth_fibonacci(n):
    # Returns n-th fibonacci number
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


def is_prime(n):
    # Return true if 'n' is prime, otherwise returns false
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