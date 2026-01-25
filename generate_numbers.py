def natural_numbers(n):
    #Returns the list of natural numbers
    return [i for i in range(1, n+1)]


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    first_num = 1
    second_num = 1

    if n == 1 or n == 2:
        return 1
    
    for _ in range(3, n+1):
        next_num = first_num + second_num
        first_num, second_num = second_num, next_num

    return second_num

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    no_of_factors = sum(1 for i in range(1, n+1) if n % i == 0)
    return no_of_factors == 2