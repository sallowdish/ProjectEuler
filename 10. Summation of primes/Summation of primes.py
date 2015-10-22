#!/usr/bin/env python3
__author__ = 'Ray'

"""
using sieve as a helper
"""

from PrimeSieve import sieve

k = 2 * 10**6

primeList = sieve(k)
print(sum(primeList))