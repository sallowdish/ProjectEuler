__author__ = 'Ray'

# set operation
multiple3 = []
multiple5 = []
multiple15 = []

for i in range(1, 1000):
    if i % 3 == 0:
        multiple3.append(i)
    if i % 5 == 0:
        multiple5.append(i)
    if i % 15 == 0:
        multiple15.append(i)

print(sum(multiple3) + sum(multiple5) - sum(multiple15))

