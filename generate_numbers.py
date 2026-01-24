def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    if n <= 0:
        return []
    return list(range(1, n + 1))


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
     # n=1 -> 0, n=2 -> 1, n=3 -> 1, n=4 -> 2 ...
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

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True