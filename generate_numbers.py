def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    if n <= 0:
        return []
    return list(range(1, n + 1))


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
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
    #Code here
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