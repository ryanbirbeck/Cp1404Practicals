
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# task a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# task b
for i in range(-20, 0, 1):
    i = i * -1
    print(i, end=' ')
print()

# task c
n = int(input('Number of stars: '))
print('*' * n)

# task d
n = int(input('Number of stars: '))
for i in range(0, n+1, 1):
    print('*' * i)
