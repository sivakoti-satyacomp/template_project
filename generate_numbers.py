# Name: Vidhatri HR
# Roll Number: 23f2000575


def natural_numbers(n):
  # Returns the list of natural numbers
  # Code here
  if n <= 0:
    return []

  numbers_list = []
  for value in range(1, n + 1):
    numbers_list.append(value)

  return numbers_list


def nth_fibonacci(n):
  # Returns n-th fibonacci number
  # Code here
  if n <= 0:
    return None

  if n == 1 or n == 2:
    return 1

  first = 1
  second = 1

  for _ in range(3, n + 1):
    next_val = first + second
    first = second
    second = next_val

  return second


def is_prime(n):
  # Return true if 'n' is prime, otherwise returns false
  # Code here
  if n <= 1:
    return False

  if n == 2:
    return True

  if n % 2 == 0:
    return False

  divisor = 3
  while divisor * divisor <= n:
    if n % divisor == 0:
      return False
    divisor += 2

  return True
