def natural_numbers(n):
    """
    Returns a list of first n natural numbers
    """
    return list(range(1, n + 1))


def nth_fibonacci(n):
    """
    Returns the nth Fibonacci number
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n):
    """
    Returns True if n is a prime number, else False
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
