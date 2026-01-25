


def natural_numbers(n):
    return list(range(1, n+1))


def nth_fibonacci(n):
    if n <= 0:
        return None
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("Natural numbers up to 10:", natural_numbers(10))
    print("10th Fibonacci number:", nth_fibonacci(10))
    print("Is 17 prime?:", is_prime(17))
