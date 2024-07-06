import unittest
from comb_sort import comb_sort

class TestCombSort(unittest.TestCase):
    def test_comb_sort(self):
        self.assertEqual(comb_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(comb_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])
        self.assertEqual(comb_sort([3, 0, 2, 5, -1, 4, 1]), [-1, 0, 1, 2, 3, 4, 5])
