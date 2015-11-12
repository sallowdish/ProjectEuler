from unittest import TestCase
from LargeSum import LargeSumBase

__author__ = 'Ray'


class TestLargeSumBase(TestCase):
  def test_loadData(self):
    obj = LargeSumBase()
    obj.loadData()
    self.assertTrue(obj.rawData)
    self.assertNotEqual(len(obj.rawData), 0)
    individualLength = len(obj.rawData[0])
    for largeNum in obj.rawData:
        self.assertEquals(individualLength, len(largeNum))
