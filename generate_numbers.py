def natural_numbers(n):
    #Returns the list of natural numbers
    return list(range(1, n + 1))


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
