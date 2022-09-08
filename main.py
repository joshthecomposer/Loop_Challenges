# Print odds 1 - 20
for i in range(1, 21):
    if i % 2 == 1:
        print(i)

# Decreasing Multiples of 3
for i in range(100, -1, -1):
    if i % 3 == 0:
        print(i)

# Print the sequence
v = 4
while v >= -3.5:
    print(v)
    v -= 1.5

# Sigma
sum = 0
for i in range(1, 101, 1):
    sum += i
print(sum)

# Factorial
product = 1
for i in range(1, 13):
    product *= i
print(product)