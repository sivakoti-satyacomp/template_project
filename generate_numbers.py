# generate_numbers.py
# Implementations for Day 2 Git/GitHub Challenge Lab

import math
from typing import List

def natural_numbers(n: int) -> List[int]:
    """
    Return a list of natural numbers from 1 to n (inclusive).
    If n is less than 1, an empty list is returned.

    Examples:
    >>> natural_numbers(5)
    [1, 2, 3, 4, 5]
    >>> natural_numbers(0)
    []
    """
    if n < 1:
        return []
    # Use simple list construction for clarity
    return list(range(1, n + 1))

def nth_fibonacci(n: int) -> int:
    """
    Return the n-th Fibonacci number using 0-based indexing:
    - nth_fibonacci(0) == 0
    - nth_fibonacci(1) == 1
    - nth_fibonacci(2) == 1

    This function uses an iterative approach which is efficient
    and easy to understand for beginners.

    Examples:
    >>> nth_fibonacci(0)
    0
    >>> nth_fibonacci(1)
    1
    >>> nth_fibonacci(7)
    13
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

def is_prime(n: int) -> bool:
    """
    Return True if n is a prime number, otherwise False.

    Note: Numbers less than 2 are not prime.

    Examples:
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    # Check odd divisors up to sqrt(n)
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True
