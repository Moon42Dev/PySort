import unittest
from radix_sort import radix_sort

class TestRadixSort(unittest.TestCase):
    def test_radix_sort(self):
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]), [2, 24, 45, 66, 75, 90, 170, 802])
        self.assertEqual(radix_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(radix_sort([]), [])
        self.assertEqual(radix_sort([1]), [1])

if __name__ == '__main__':
    unittest.main()
