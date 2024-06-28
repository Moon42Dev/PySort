import unittest
from heap_sort import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_heap_sort(self):
        self.assertEqual(heap_sort([4, 10, 3, 5, 1]), [1, 3, 4, 5, 10])
        self.assertEqual(heap_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(heap_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])
