__author__ = 'Ray'
# Brute force

def squareofSum(n):
    return sum([i for i in range(1,n+1)]) ** 2

def sumofSquare(n):
    return sum([i**2 for i in range(1,n+1)])

n = 100
print(abs(squareofSum(n) - sumofSquare(n)))