__author__ = 'Ray'
# brute force

import HDTN
import math

class HDTNBrute(HDTN.HDTN):

    @staticmethod
    def factorize(n):
        factors = []
        for i in range(1, int(math.sqrt(n))+1):
            if n%i == 0:
                factors.append(i)
                if int(n/i) != i:
                    factors.append(int(n/i))
        return factors

    @staticmethod
    def search(upperBound):
        i = 1
        factors = HDTNBrute.factorize(1)
        while(len((factors)) < upperBound):
            i += 1
            factors = HDTNBrute.factorize(HDTNBrute.computeTriangularNumber(i))
        return (HDTNBrute.computeTriangularNumber(i),factors.sort())