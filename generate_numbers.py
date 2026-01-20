def natural_numbers(n):
    #Returns the list of natural numbers
  n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)



def nth_fibonacci(n):
    #Returns n-th fibonacci number
   n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
