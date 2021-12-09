def full_prime(n):   
    while (n) :
        num = n % 10        
        if (num != 2 and num!= 3 and num != 5 and num != 7) :
            return 0
        n = n / 10
        return 1
def prime(n):
    if (n == 1):
        return 0
    i = 2
    while i * i <= n :
        if (n % i == 0):
            return 0
        i = i + 1
    return 1
def isFullPrime(n) :
    return (full_prime(n) and prime(n))
n = int(input())
if (isFullPrime(n)) :
    print("full_prime")
else :
    print("not_a_full_prime")
"""
53
full_prime
>>> 
============= RESTART: C:/Users/ADMIN/Desktop/python/full_prime.py =============
57
not_a_full_prime
>>>
"""
