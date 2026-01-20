def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    return [i for i in range(1, n+1)]


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    if n <= 1:
        return n
    return nth_fibonacci(n-1) + nth_fibonacci(n-2)
    

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    if n <=1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
