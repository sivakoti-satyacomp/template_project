def natural_numbers(n):
    """Return first n natural numbers (1, 2, 3, ... n)"""
    return list(range(1, n+1))

def nth_fibonacci(n):
    """Return nth Fibonacci number (0, 1, 1, 2, 3, 5, 8...)"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def is_prime(n):
    """Check if n is prime number"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test functions
if __name__ == "__main__":
    print("Natural numbers (5):", natural_numbers(5))
    print("5th Fibonacci:", nth_fibonacci(5))
    print("Is 17 prime?", is_prime(17))
    print("Is 15 prime?", is_prime(15))
