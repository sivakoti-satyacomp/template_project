def natural_numbers(n):
    """
    Returns a list of the first n natural numbers.
    Assumption: Natural numbers start from 1.
    Example: n=5 -> [1, 2, 3, 4, 5]
    """
    if n < 1:
        return []
    return list(range(1, n + 1))


def nth_fibonacci(n):
    """
    Returns the n-th Fibonacci number.
    Assumption:
    F(0) = 0
    F(1) = 1
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

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
    Returns True if n is a prime number, otherwise False.
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
