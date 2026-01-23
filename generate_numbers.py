def natural_numbers(n):

    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        return []

    return list(range(1, n + 1))


def nth_fibonacci(n):

    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


def is_prime(n):

    if not isinstance(n, int):
        return False

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True
