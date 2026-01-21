def natural_numbers(n):
    # Returns the list of first n natural numbers
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers


def nth_fibonacci(n):
    # Returns n-th Fibonacci number
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def is_prime(n):
    # Returns True if n is prime, otherwise False
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
