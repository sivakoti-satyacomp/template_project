def natural_numbers(n):
    #Returns the list of natural numbers
    """Return a list of the first n natural numbers: [1, 2, ..., n].
    Assumes n is a non-negative integer. If n <= 0, returns empty list.
    """
    if n <= 0:
        return []
    return list(range(1, n + 1))


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    """Return the n-th Fibonacci number using the convention:
    nth_fibonacci(1) == 0, nth_fibonacci(2) == 1
    So sequence is: 0, 1, 1, 2, 3, 5, ...
    If n <= 0, raise ValueError.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    # small n shortcuts
    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    """Return True if n is prime, otherwise False.
    By convention, numbers < 2 are not prime.
    Works for positive integers.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    # test odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True