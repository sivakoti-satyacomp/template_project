def natural_numbers(n):
    # Returns the list of first n natural numbers (starting from 1)
    if n < 1:
        return []
    return list(range(1, n + 1))


def nth_fibonacci(n):
    # Returns n-th Fibonacci number (0-indexed)
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
    # Return True if 'n' is prime, otherwise False
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
