# Problem 4 - Largest palindrome product
""" A palindromic number reads the same both ways. The
largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of
two 3-digit numbers."""

# Just going to guess that the number should be at
# least 950

start_num = 100
pair= [1, 1]
for i in range(start_num, 1000):
    for j in range(start_num, 1000):
        prod = i*j
        num_str= str(prod)
        if num_str == num_str[-1::-1] and pair[0]*pair[1] <prod:
            pair = [i, j]

print(pair)
#print(f'{pair[0]} and {pair[1]} max the palindrome {pair[0]*pair[1]}, the maximal palidrome from the product of two 3-digit numbers')
