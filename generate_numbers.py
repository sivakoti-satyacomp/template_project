def natural_numbers(n):
    # Returns a list of numbers from 1 to n
    return list(range(1, n + 1))

def nth_fibonacci(n):
    # Returns the nth number in the Fibonacci sequence (0, 1, 1, 2, 3...)
    if n <= 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def is_prime(n):
    # Returns True if n is prime, else False
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

    if __name__ == "__main__":
    print(f"First 5 natural numbers: {natural_numbers(5)}")
    print(f"The 7th Fibonacci number: {nth_fibonacci(7)}")
    print(f"Is 13 prime?: {is_prime(13)}")