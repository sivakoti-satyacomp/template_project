def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    n = int(input("Enter a number: "))

    for i in range(1, n + 1):
        print(i)



def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    n = int(input("Enter n: "))

    if n <= 0:
        print("Please enter a positive number")
    elif n == 1:
        print("Fibonacci number at position 1 is 0")
    elif n == 2:
       print("Fibonacci number at position 2 is 1")
    else:
        a, b = 0, 1
        for i in range(3, n + 1):
            a, b = b, a + b
        print(f"Fibonacci number at position {n} is {b}")


def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    if (n <= 1):
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if (n % i == 0):
            return False
    return True
print(is_prime(24))