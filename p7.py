""" Problem 7 - 10 001st prime number"""


def isPrime(number, p_list):
    for prime in p_list:
        if not number % prime:
            return False
    return True

primes = [2]
p_counter = 1
num = 3
while p_counter != 10001:
    if isPrime(num, primes):
        primes.append(num)
        p_counter += 1
    num += 2
print(len(primes))
print(primes[-1])
