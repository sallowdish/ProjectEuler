__author__ = 'Ray'

import HDTN
import math


class HDTNBruteFocus(HDTN.HDTN):
    @staticmethod
    def factororCount(n):
        if n <= 0:
            return 0
        if n == 1:
            return n
        if n == 2 or n == 3:
            return  2
        c = 0
        for i in range(1, int(math.sqrt(n))):
            if n % i == 0:
                c += 2
        if n % math.sqrt(n) == 0:
            c += 1
        return c
