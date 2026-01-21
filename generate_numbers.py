def natural_numbers(n):
    #Returns the list of natural numbers
    numbers= []
    for i in range(1,n+1):
        numbers.append(i)
    return numbers

def nth_fibonacci(n):
    #Returns n-th fibonacci number
    a= 0
    b= 1
    if n==1:
        return a
    elif n==2:
        return b
    else:
        for i in range(2, n):
            c= a+b
            a=b
            b=c
        return c
    
def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    if n<=1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True