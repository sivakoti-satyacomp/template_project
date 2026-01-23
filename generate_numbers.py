def natural_numbers(n):
  """
  Return list of first n natural numbers starting from 1.
  """
  if n <= 0:
    return []

  return list(range(1, n + 1))


def nth_fibonacci(n):
  """
  Return nth Fibonacci number (1-indexed).
  Fibonacci: 1, 1, 2, 3, 5, ...
  """
  if n <= 0:
    return None

  if n == 1 or n == 2:
    return 1

  a, b = 1, 1
  for _ in range(3, n + 1):
    a, b = b, a + b

  return b


def is_prime(n):
  """
  Return True if n is prime, else False.
  """
  if n <= 1:
    return False

  if n == 2:
    return True

  if n % 2 == 0:
    return False

  i = 3
  while i * i <= n:
    if n % i == 0:
      return False
    i += 2

  return True
