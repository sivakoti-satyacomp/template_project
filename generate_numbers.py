def natural_numbers(n: int):
    #Returns the list of natural numbers
    #Code here
    num_list = []
    for i in range(n):
        num_list.append(i+1)
    
    return num_list


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a,b,c= 0,1,0
        for i in range(3,n+1):
            c = b
            b += a
            a = b
        return b


def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    for i in range(1,(int(n**0.5)+1)):
        if n % i == 0 and (i != 1 or i != n):
            return False
    return True 