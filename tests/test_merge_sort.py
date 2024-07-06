import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1]), [1])

if __name__ == '__main__':
    unittest.main()
