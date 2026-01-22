def natural_numbers(n):
    # Returns the list of natural numbers
    return list(range(1, n + 1))


def nth_fibonacci(n):
    # Returns n-th fibonacci number
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1

    a = 0
    b = 1

    for i in range(n - 2):
        a, b = b, a + b
    return b


def is_prime(n):
    # Return true if 'n' is prime, otherwise returns false
    if n == 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# Test methods
# print(natural_numbers(20))
# print(nth_fibonacci(5))
# print(is_prime(23))
