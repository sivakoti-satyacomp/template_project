def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    for i in range(1, n + 1):
        print(i, end=' ')
    print()


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    if n <= 0:
        return None  # or raise an error if you want
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    if n <= 1:
        return False  # 0 and 1 are not prime
    if n <= 3:
        return True   # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # multiples of 2 or 3 are not prime

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True