import unittest
from quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(quick_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([1]), [1])

if __name__ == '__main__':
    unittest.main()
