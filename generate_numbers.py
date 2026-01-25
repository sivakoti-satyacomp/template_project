def natural_numbers(n):
    #Returns the list of natural numbers
    # nat_list = []
    # for i in range(1, n+1):
    #     nat_list.append(i)
    # return nat_list

    return list(range(1, n+1))

def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here

    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a,b = 0,1
        for _ in range(3, n+1):
            a,b = b, a + b
        return b

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here

    if n<=1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True