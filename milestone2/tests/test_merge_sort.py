# https://docs.python.org/3/library/unittest.html
import unittest

from milestone2.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_length(self):
        items = ['t', 'e', 's', 't', 'l', 'e', 'n', 'g', 't', 'h']
        self.assertEqual(len(items), len(merge_sort(items)))


if __name__ == '__main__':
    unittest.main()
