def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    l=[]
    for i in range(1,n+1):
        l.append(i)
    return l


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return nth_fibonacci(n-1)+nth_fibonacci(n-2)


def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    return n%2==0
