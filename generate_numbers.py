def natural_numbers(n):
    #Returns the list of natural numbers
    if n < 1:
        return "Invalid input"
    return [n_ for n_ in range(1,n)]


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    if n < 1:
        return "Invalid input"
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    if n < 2:
        return False
    for n_ in range(2, n):
        if n % n_ == 0:
            return False
    return True


