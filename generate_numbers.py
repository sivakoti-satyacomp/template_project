def natural_numbers(n):
    """Returns the list of natural numbers from 1 to n"""
    if n < 1:
        return []
    return list(range(1, n + 1))


def nth_fibonacci(n):
    """Returns n-th fibonacci number (0-indexed)"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Iterative approach for efficiency
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n):
    """Return true if 'n' is prime, otherwise returns false"""
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