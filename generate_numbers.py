def natural_numbers(n):
    """
    Returns the list of first n natural numbers
    Example: n = 5 -> [1, 2, 3, 4, 5]
    """
    if n <= 0:
        return []
    return list(range(1, n + 1))


def nth_fibonacci(n):
    """
    Returns the n-th Fibonacci number
    Example: n = 1 -> 0
             n = 2 -> 1
             n = 6 -> 5
    """
    if n <= 0:
        return None
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
    Returns True if n is a prime number, otherwise False
    """
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
