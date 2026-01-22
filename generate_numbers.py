def natural_numbers(n):
    # Returns the list of natural numbers
    return list(range(1, n + 1))


def nth_fibonacci(n):
    # Returns n-th fibonacci number
    pass


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
# print(is_prime(23))
