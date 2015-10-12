__author__ = 'Ray'
# naive nested loop

max = 0
for i in range(999,99,-1):
    for j in range(i, 99, -1):
        product = i*j
        if str(product) == str(product)[::-1] and product>max:
            max = product
print(max)