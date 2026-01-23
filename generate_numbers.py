def natural_numbers(n):
    #Returns the list of natural numbers
    numlist = []
    for i in range(1, n+1):
        numlist.append(i)
    return numlist    
    
def nth_fibonacci(n):
    #Returns n-th fibonacci number
    if n <= 1:
        return n
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  
    return True


