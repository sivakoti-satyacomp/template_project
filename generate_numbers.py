# list of first n natural numbers
def natural_numbers(n):
    return list(range(1, n + 1))
# nth fibonacci number
def nth_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
# Returns True if n is prime, False otherwise
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True