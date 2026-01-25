def natural_numbers(n):
    #Returns the list of natural numbers
    return [i for i in range(1,n+1)]


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    if(n<=1):
        return 0
    if(n<3):
        return 1
    return nth_fibonacci(n-1)+nth_fibonacci(n-2)


def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    if(n<2):
        return False
    for i in range(2,n-1):
        if(n%i==0):
            return False
    return True
        
    