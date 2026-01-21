def natural_numbers(n):
    """Return a list of first n natural numbers"""
    return list(range(1, n + 1))


def nth_fibonacci(n):
    """Return the nth Fibonacci number"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

