__author__ = 'Ray'

import unittest
from HDTNBrute import HDTNBrute
from HDTNBruteFocus import HDTNBruteFocus
from HDTNSmart import HDTNSmart

class FunctionalityTest(unittest.TestCase):
    def test_correctless_small_number(self):
        self.assertEqual(HDTNBrute.search(4)[0], 6)

    def test_correctless_small_number2(self):
        self.assertEqual(HDTNBrute.search(5)[0], 28)

    def test_correctless_large_number(self):
        k=500
        while(1):
            n = HDTNBrute.computeTriangularNumber(k)
            factors = HDTNBrute.factorize(n)
            if len(factors) > 500:
                break
            k += 1
        self.assertEquals(HDTNBrute.computeTriangularNumber(k), 76576500)

class SubComponentTest(unittest.TestCase):
    def test_factorize(self):
        for i in range(1,30):
            n = HDTNBrute.computeTriangularNumber(i)
            print("{0:2d}|{1:5d}|{2}".format(i, n, HDTNBrute.factorize(n)))

class ImprovementTest(unittest.TestCase):
    def test_improvement(self):
        k=500
        i = 500
        while(1):
            n = HDTNBruteFocus.computeTriangularNumber(i)
            if HDTNBruteFocus.factororCount(n) >= k:
                break
            i += 1
        self.assertEquals(HDTNBruteFocus.computeTriangularNumber(i), 76576500)

class SmartTest(unittest.TestCase):
    def test_smartcount(self):
        k = 500
        self.assertEquals(HDTNSmart.search(k)[1], 76576500)

if __name__ == '__main__':
    unittest.main()
