def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        return []

    return list(range(1, n + 1))


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here