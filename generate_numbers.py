def natural_numbers(n):
    numbers = []          

    for i in range(1, n + 1):   
        numbers.append(i)       

    return numbers         



def nth_fibonacci(n):
    #Returns n-th fibonacci number
    # handle invalid input
    if n <= 0:
        return None
    # first fibonacci number
    if n == 1:
        return 0
    # second fibonacci number
    if n == 2:
        return 1
    # starting values
    first = 0
    second = 1
    # calculate from 3rd to nth number
    for i in range(3, n + 1):
        next_value = first + second
        first = second
        second = next_value

    return second

print(nth_fibonacci(9))

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    # numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # check each number from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    # if no number divides n, it is prime
    return True
