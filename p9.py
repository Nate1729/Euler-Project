""" Problem 9 - Special Pythagorean Triplet
A Pythagorean triplet is a set of three natural
numbers, a<b<c, for which
    a^2 + b^2 = c^2
For example, 3^2+4^2=5^2

There exits exactly one Pythagorean triplet for which
a+b+c = 100. Find the product abc."""
from math import ceil
s = 1000
found = False
for a in range(2, ceil(s/3)):
    for b in range(a, ceil(s/2)):
        c = s - a - b

        if (a*a + b*b) == c*c:
            found = True
            break
    if found:
        break

print(f'The triple is {a}, {b}, {c}, and product is {a*b*c}')
