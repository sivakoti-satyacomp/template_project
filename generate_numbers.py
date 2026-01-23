import math

def get_number(n):
    while True:
        try:
            return int(n)                       # Try to convert to integer 
        except ValueError:
            print("Please enter a valid(integer) number")
            return 0

def natural_numbers(n):                         # Returns the list of natural numbers
    
    if get_number(n) == 0: return 0
    else: n = get_number(n)

    if n <= 0: return[]                        # Appendment starts after 0
    
    return list(range(1, n+1)) 


def nth_fibonacci(n):                           # Returns n-th fibonacci number
    
    if get_number(n) == 0: return 0
    else: n = get_number(n)

    a = 1
    b = 1

    if n <= 0: return 0                         # Natural fibonacci series 
             

    elif n == 1 or n == 2: return 1             # First two digit are 1 

    for i in range(3, n+1): 
        a, b = b, a+b                           # fibonacci series count up
    
    return b


def is_prime(n):                                # Return true if 'n' is prime, otherwise returns false
    
    if get_number(n) == 0: return 0
    else: n = get_number(n)

    if (n <= 1) or (n%2 == 0): return False              # even num multiple of 2

    elif n == 2: return True

    else:
        is_prime = True
        max_div = math.floor(math.sqrt(n))      # Flag variable

        for i in range(3, max_div + 2):         # filtering for odd num
            if n % i == 0:                      # check limited to sqrt(n)
                is_prime = False
                print(i)
                break
        
        return is_prime


#output test
#print(natural_numbers(input("Enter (natural_numbers): ")))
#print(nth_fibonacci(input("Enter (nth_fibonacci) : ")))
#print(is_prime(input("Enter (is_prime): ")))