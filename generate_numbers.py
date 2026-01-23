import math
from typing import List

def natural_numbers(n: int) -> List[int]:
    """
    Returns a list of the first n natural numbers starting from 1.
    """
    if n < 0:
        return []
    return list(range(1, n + 1))

def nth_fibonacci(n: int) -> int:
    """
    Returns the n-th Fibonacci number using an iterative approach 
    for O(n) time complexity.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def is_prime(n: int) -> bool:
    """
    Determines if a number is prime using the square root rule.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check factors from 5 up to sqrt(n)
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True