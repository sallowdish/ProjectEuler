__author__ = 'Ray'
# sum of different terms

def sumSquareDiff(n):
    sum = 0
    lst = [i for i in range(1, n+1)]
    for i in lst:
        for j in lst:
            if i != j:
                sum += i*j
    return sum

n = 100
print(sumSquareDiff(n))