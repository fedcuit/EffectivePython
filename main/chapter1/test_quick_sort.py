from unittest import TestCase

from main.chapter1.quicksort import quick_sort


__author__ = 'edfeng'


class TestQuickSort(TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort([9, 8, 4, 5, 32, 64, 2, 1, 0, 10, 19, 27]),
                         [0, 1, 2, 4, 5, 8, 9, 10, 19, 27, 32, 64])