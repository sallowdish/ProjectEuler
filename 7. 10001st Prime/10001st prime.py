__author__ = "Ray"

# pi(x) which notes the prime count function
# it returns the #prime smaller than x
# by looking at the table here: https://en.wikipedia.org/wiki/Prime-counting_function#Table_of_.CF.80.28x.29.2C_x_.2F_ln_x.2C_and_li.28x.29
# we know the closet upper bound to use in sieve(n) in the power of 10

from PrimeSieve import sieve

# sieve

n = 1000000

print(list(sieve(n))[10000])