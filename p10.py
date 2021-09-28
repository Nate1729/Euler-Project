""" Problem 10 - Summation of primes
The sum of the primes below 10 is 2+3+5+7=17

Find the sum of the primes below two million"""

def isPrime(test_number, prime_list):
    for prime in prime_list:
        if not test_number % prime:
            return False
    return True

upper_bound = 2*(10**6)
prime_list = []
for num in range(2, upper_bound):
    print(num)
    if isPrime(num, prime_list):
        prime_list.append(num)

print(f'The sum of all primes less than {upper_bound} is {sum(prime_list)}')
