def natural_numbers(n):
    #Returns the list of natural numbers
    #Code here
    total = n * (n + 1) // 2
    print("Sum:", total)



def nth_fibonacci(n):
    #Returns n-th fibonacci number
    #Code here
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def is_prime(n):
    #Return true if 'n' is prime, otherwise returns false
    #Code here
    if n<= 1:
       print("Not a prime number")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if n% i == 0:
               print("Not a prime number")
               break
            else:
                print("Prime number")

