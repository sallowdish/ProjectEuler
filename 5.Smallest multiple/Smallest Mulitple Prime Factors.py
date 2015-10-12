__author__ = "Ray"
# prime factorization

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

    primes = sieve(n)
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

def primeCount(n):
    """
    find the prime factors of given integer
    :param n: a natural integer
    :return: factors in format of counting
    """
    prime_count = [0 for x in range(k)]
    prime_factor = prime_factorization(n)
    for p in prime_factor:
        prime_count[int(p)-1]+=1
    return  prime_count

def mergeFactor(primeCount1, primeCount2):
    if len(primeCount1) != len(primeCount2):
        return []
    for i in range(len(primeCount1)):
        primeCount1[i] = max(primeCount1[i], primeCount2[i])
    return primeCount1



k = 20

prime_factors = map(lambda x: primeCount(x), range(1,k+1))
prime_counts = reduce(lambda a,b: mergeFactor(a,b), prime_factors)
lcm = 1
for index in range(len(prime_counts)):
    product = (index+1) ** prime_counts[index]
    lcm *= product
print(lcm)