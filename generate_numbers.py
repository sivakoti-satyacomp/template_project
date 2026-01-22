# template_project – function implementations

def natural_numbers(n):
    """Return the first n natural numbers in a list."""
    return [i for i in range(1, n + 1)]

def nth_fibonacci(n):
    """Return the n-th Fibonacci number (0-indexed)."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(n):
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    # Example usage:
    print("First 5 natural numbers:", natural_numbers(5))
    print("6th Fibonacci number:", nth_fibonacci(6))
    print("Is 17 prime?", is_prime(17))
