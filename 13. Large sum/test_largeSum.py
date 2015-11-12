from unittest import TestCase
from LargeSum import LargeSum
__author__ = 'Ray'


class TestLargeSum(TestCase):
    def test_sumUp(self):
        instance = LargeSum()
        instance.loadData("smallData.in")
        result = instance.sumUp()
        self.assertEquals("48191923814493780126", result)

    def test_largeNum_sumUp(self):
        instance = LargeSum()
        result = instance.sumUp()
        self.assertEquals("5537376230390876637302048746832985971773659831892672", result)