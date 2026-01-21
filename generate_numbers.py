def natural_numbers(n):
    """
    Returns a list of first n natural numbers.
    Natural numbers are assumed to start from 1.
    """
    if n <= 0:
        return []
    return list(range(1, n + 1))


def nth_fibonacci(n):
    """
    Returns the n-th Fibonacci number.
    Assumes:
    F(1) = 0
    F(2) = 1
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
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

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True
