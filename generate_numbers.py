def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    
