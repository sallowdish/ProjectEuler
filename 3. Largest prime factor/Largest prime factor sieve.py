__author__ = 'Ray'

from functools import reduce
def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

def prime_factorization(n):
    """
    :param n: a natural integer
    :return: a list of prime factors of n
    """

    primes = sieve(10000)
    factor = []
    for p in primes:
        if p**2 > n:
            break
        while n % p ==0:
            # n is dividable by p
            factor.append(p)
            n /= p
    # all primes have been attempted
    if n > 1:
        factor.append(n)
    return factor

k = 6857.0
print(prime_factorization(k))
