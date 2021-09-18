# Find the sum of all multiples of 3 and 5

total = 0
for num in range(3, 1000):
    if not num % 3:
        total += num
    elif not num % 5:
        total += num

print(f"The sum of multiples of 3 and 5 is {total}")
