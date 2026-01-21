# math_functions.py

def natural_numbers(n):
    """Return a list of natural numbers from 1 to n."""
    if n < 1:
        return []
    return list(range(1, n + 1))


def nth_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return None
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return a


def is_prime(n):
    """Return True if n is prime, else False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

