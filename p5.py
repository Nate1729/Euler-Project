""" Problem 5 - Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers 1 to 10
without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20"""
from math import log, floor


# First we need all of the primes
top = 20

def isPrime(num, prime_list):
    for p in prime_list:
        if not num % p:
            return False
    return True

def findExp(num, top):
    # Solve the equation 2^x = top
    # round down which we can just do with int
    return floor(log(top, num))

primes = []
powers = []
for num in range(2, top+1):
    if isPrime(num, primes):
        primes.append(num)
        powers.append(findExp(num, top))

# Calculating everything
total = 1
for prime, power in zip(primes, powers):
    total = total * (prime**power)

print(f'The total is {total}')
