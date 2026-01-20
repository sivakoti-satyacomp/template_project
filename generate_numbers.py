def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    nat_num_list = []
    for i in range(1, n+1):
        nat_num_list.append(i)
    return nat_num_list


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    if n <= 0: return 0
    elif n == 1: return 1
    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
    

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    limit = int(math.sqrt(n)) + 1    
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True
