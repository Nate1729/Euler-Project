# Problem 3 Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13, 29.
# What is the largest prime factor of the number
# 600851475143


NUM = 600851475143

def find_min_div(number):
    for i in range(2, number+1):
        if not number % i:
            return i
    return Error()

factors = []
num = NUM
while num != 1:
    factors.append(find_min_div(num))
    num = num // factors[-1]

print(f'The maximum prime factor of {NUM} is {max(factors)}')
