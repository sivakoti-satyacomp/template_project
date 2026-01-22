def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    for i in range(n+1):
        print(i)


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    if n <= 1:
        return n
    else:
        # Recursively call the function for the previous two numbers
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    return  n%2!=0
