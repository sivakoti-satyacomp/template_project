def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    nat_numbers = []
    for i in range(1, n+1):
        nat_numbers.append(i)
    return nat_numbers


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    if n < 0: return 'enter a number >= 0'
    if n in [0, 1]:
        return n
    
    a,b = 0,1
    for _ in range(2, n+1):
        a,b = b, a+b
    
    return b

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
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