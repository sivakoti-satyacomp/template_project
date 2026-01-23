def natural_numbers(n):
        return [i for i in range(n+1)]


def nth_fibonacci(n):
    #Returns n-th fibonacci number
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def is_prime(n):
        count=0
        while i>0:
                if n%i==0:
                        count+=1
                i+=1
        if count==2:
                return True
        else:
                return False
                        