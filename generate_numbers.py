def natural_numbers(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n <= 0:
        raise ValueError("Input must be a positive integer")

    return list(range(1, n + 1))
    #Returns the list of natural numbers up to 'n'


def nth_fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
    #Returns the nth Fibonacci number

def is_prime(n):
    def is_prime(n):
    if not isinstance(n, int):
        return False

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
    #Returns True if 'n' is a prime number, else False