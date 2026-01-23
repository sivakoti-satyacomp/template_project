def natural_numbers(n):
    for i in range (1,n):
        return i


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    fact=[]
    for i in range (1,n+1):
        if n%i==0:
            fact.append(i)
    if len(fact==2):
        return True
    else:
        return False