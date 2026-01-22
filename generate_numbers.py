def natural_numbers(n):
    """
    Returns a list of the first n natural numbers starting from 1.

    Parameters:
    n (int): Number of natural numbers to generate

    Returns:
    list: List of natural numbers from 1 to n
    """

    # If n is zero or negative, return an empty list
    if n <= 0:
        return []

    # Generate and return natural numbers from 1 to n
    return list(range(1, n + 1))



def nth_fibonacci(n):
    """
    Returns the nth Fibonacci number (1-based indexing).

    Fibonacci sequence:
    0, 1, 1, 2, 3, 5, 8, ...

    Parameters:
    n (int): Position in Fibonacci sequence

    Returns:
    int: nth Fibonacci number
    """

    # Invalid input check
    if n <= 0:
        return None

    # Base cases
    if n == 1:
        return 0
    if n == 2:
        return 1

    # Initialize first two Fibonacci numbers
    a, b = 0, 1

    # Compute Fibonacci numbers iteratively
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


def is_prime(n):
    """
    Checks whether a number is a prime number.

    Parameters:
    n (int): Number to be checked

    Returns:
    bool: True if prime, False otherwise
    """

    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # Eliminate even numbers greater than 2
    if n % 2 == 0:
        return False

    # Check divisibility from 3 to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

