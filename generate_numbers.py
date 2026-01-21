def natural_numbers(n):
    return [x for x in range(1,n+1)]

def nth_fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

