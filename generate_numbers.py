def natural_numbers(n):
    """
    Returns a list of the first n natural numbers (starting from 1).
    
    Args:
        n (int): The number of natural numbers to generate.
    
    Returns:
        list: A list containing natural numbers from 1 to n.
    """
    return list(range(1, n + 1))

def nth_fibonacci(n):
    """
    Returns the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
    
    Returns:
        int: The nth Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a    

def is_prime(num):
    """
    Checks if a number is prime.
    
    Args:
        num (int): The number to check for primality.
    
    Returns:
        bool: True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True