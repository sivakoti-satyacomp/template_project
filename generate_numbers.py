def natural_numbers(n):
    #Returns the list of natural numbers
    return list(range(1, n + 1))


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    if n <= 0:
        return None
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
    return n%2==0