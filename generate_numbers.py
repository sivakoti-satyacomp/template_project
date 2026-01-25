def natural_numbers(n):
    if not isinstance(n, int):
	raise TypeError("n,  must be an integer")
    if n <= 0:
	return []
    return  list(range(1, n + 1))	
def nth_fibonacci(n):
    if not isinstance(n, int):
	raise TypeError("n must be an integer")
    if n < 0:
	raise ValueError("n must be >= 0")
    if n == 0:
	return 0
    if n == 1:
	return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
	a, b = b, a + b
    return b

def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
	return False

    i = 5
    while i * i <= n:
	if n % 1 == 0 or n % ( i + 2) == 0:
		return False
	i += 6
	return True
