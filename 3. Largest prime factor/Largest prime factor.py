__author__ = 'Ray'

from functools import reduce

def prime_factor(n):
    """
    :param n: an integer
    :return: a list of all prime factor
    """
    if n < 0:
        return []


    k = 3
    factor = []
    if n % 2 == 0:
        factor.append(2)
    while n % 2 ==0:
        n /= 2
    while n > 1:
        if n % k == 0:
            factor.append(k)
            while n % k == 0:
                n /= k
        k += 2
    return factor

n = 600851475143
print(prime_factor(n))
