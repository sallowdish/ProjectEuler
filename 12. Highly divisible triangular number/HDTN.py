__author__ = "Ray"

class HDTN:

    @staticmethod
    def computeTriangularNumber(n):
        if n <= 0: return 0
        if n == 1: return 1
        return int(n*(n+1)/2)
