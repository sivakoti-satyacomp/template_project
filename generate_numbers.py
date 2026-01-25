def natural_numbers(n: int) -> list[int]:
    """Return a list of natural numbers from 1 to n."""
    return list(range(1, n + 1))


def nth_fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number (1-indexed: F1 = 0, F2 = 1)."""
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


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, else False."""
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
