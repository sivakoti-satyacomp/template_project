def natural_numbers(n):
    #Returns the list of natural numbers
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    a = 0
    b = 1
    for i in range(2,n+1):
        a , b = b , a+b
    return b
        

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    if n <= 1:
        print(False)
    else:
        is_prime = True  # Flag variable
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    return(is_prime)

print(natural_numbers(6))
print(nth_fibonacci(10))
print(is_prime(17))