""" for solving this problem we use a mathematic method called The Sieve of Eratosthenes
this method take prime numbers and then delete all nonprime numbers to the targert
"""
def sieveOfEratosthenes(target):
    prime = [True] * (target+1)
    prime[0], prime[1] = False,False #because 0 and 1 are not primes
    p=2#this is the smallest prime number
    while (p*p) <= target:
        if prime[p]:
            for i in range(p*p,target+1,p):
                prime[i] = False
        p += 1
    return [i for i in range(target+1) if prime[i]]
primeList = sieveOfEratosthenes(2000000)
sum = 0
for i in primeList:
    sum += i
    
print("sum of the prime numbers smaller than 2000000 is :", sum)

'''developed by Mehrab_mahmoudifar
    difficulty level : 5%
    Thank You ♥
    '''