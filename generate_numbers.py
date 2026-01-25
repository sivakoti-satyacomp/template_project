def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    return list(range(1, n))

def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    sqrt_5 = 5 ** 0.5
    return int((((1+sqrt_5)/2)**n-((1-sqrt_5)/2)**n)/sqrt_5)

def is_prime(n, i=2):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    return n >= 2 and (i >= n or bool(n % i) and is_prime(n, i + 1))
