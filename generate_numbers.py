def natural_numbers(n):
    # Returns the list of natural numbers from 1 to n
    if n < 1:
        return []
    return list(range(1, n + 1))
print("natural_numbers(5)",natural_numbers(5))


def nth_fibonacci(n):
    """
    Calculates the nth Fibonacci number iteratively.
    Uses 0-based indexing (e.g., n=4 returns 3).
    """
    if n < 0:
        return "Incorrect input, n cannot be negative"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

# Example Usage:
n = 11
print(f"The {n}th Fibonacci number is: {nth_fibonacci(n)}") # Output: The 9th Fibonacci number is: 34


import math


def is_prime(n):
    # Return true if 'n' is prime, otherwise returns false
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Eliminate multiples of 2 and 3 quickly
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisors from 5 to sqrt(n)
    # We skip even numbers by incrementing by 6 (checking 6k ± 1)
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True
print("is_prime(5)",is_prime(5))