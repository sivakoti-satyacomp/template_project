def natural_numbers(n):
    #Returns the list of natural numbers
    ls = []
    while n>0:
        ls.append(n)
        n-=1
    return n


def nth_fibonacci(n):
    #Returns n-th fibonacci numbe
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
        

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    limit = int(n**(1/2)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True
