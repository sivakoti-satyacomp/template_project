def natural_numbers(n):
    """
    Returns a list of natural numbers from 1 to n (inclusive).
    """
    if n <= 0:
        return []
    return list(range(1, n + 1))


def nth_fibonacci(n):
    """
    Returns the n-th Fibonacci number.
    F(0) = 0, F(1) = 1
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def is_prime(n):
    """
    Returns True if n is prime, otherwise False.
    """
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
