__author__ = 'Ray'
# naive linear checking
from functools import reduce
def gcd(a,b):
    # Euclidean algorithm
    # https://en.wikipedia.org/wiki/Euclidean_algorithm#Euclidean_division
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a,b):
    # Reduction by gcd
    # https://en.wikipedia.org/wiki/Least_common_multiple#Reduction_by_the_greatest_common_divisor
    if a < b:
        (a,b) = (b,a)
    if a % b ==0:
        return a
    else:
        return a*b/gcd(a,b)

k = 20
lst = list(range(k,0,-1))
lcm = reduce(lambda a,b:lcm(a,b), lst)
print(lcm)