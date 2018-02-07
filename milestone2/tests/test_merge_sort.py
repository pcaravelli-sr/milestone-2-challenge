# https://docs.python.org/3/library/unittest.html
import unittest

from enum import Enum

from milestone2.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([], merge_sort([]))

    def test_singleton(self):
        self.assertEqual([1], merge_sort([1]))
        self.assertEqual(['x'], merge_sort(['x']))

    def test_two_items(self):
        self.assertEqual([1, 2], merge_sort([1, 2]))
        self.assertEqual([1, 2], merge_sort([2, 1]))
        self.assertEqual(['x', 'y'], merge_sort(['x', 'y']))
        self.assertEqual(['x', 'y'], merge_sort(['y', 'x']))

    # TODO: add at least 3 more test cases here!

    def test_sort_is_stable(self):
        """
        One of the important features of merge sort is that it is stable. This means that the pre-existing
        order of equal items in the list will be preserved. This can be a desirable feature for some use-
        cases. For example, it allows us to sort a list of persons by first name, and then sort it again
        by last name. The result will be a list sorted by last name, then first name (when last names are
        the same).

        Note: to achieve this, the Person class overrides the comparison operators so we can compare using
        < <= == != >= > operators, and exposes the ability to change whether this compares by first, last,
        or both names via the `Person.comparison_mode` variable. This is a bit of a hack to allow us to use
        our `merge_sort` function as is. For reference, Python's built-in sorting functions achieve this in
        a far more elegant fashion: https://wiki.python.org/moin/HowTo/Sorting#Key_Functions
        """
        names = [
            ('Jennifer', 'Jones'),
            ('Jane', 'Doe'),
            ('Daniel', 'Smith'),
            ('John', 'Doe'),
            ('Jason', 'Jones'),
            ('Andrew', 'Smith'),
            ('David', 'Adams')
        ]
        persons = [Person(first, last) for (first, last) in names]

        Person.comparison_mode = Person.ComparisonMode.FIRST_NAME
        sorted_persons = merge_sort(persons)

        Person.comparison_mode = Person.ComparisonMode.LAST_NAME
        sorted_persons = merge_sort(sorted_persons)

        expected_names = [
            ('David', 'Adams'),
            ('Jane', 'Doe'),
            ('John', 'Doe'),
            ('Jason', 'Jones'),
            ('Jennifer', 'Jones'),
            ('Andrew', 'Smith'),
            ('Daniel', 'Smith')
        ]
        expected_persons = [Person(first, last) for (first, last) in expected_names]

        Person.comparison_mode = Person.ComparisonMode.BOTH_NAMES

        self.assertEqual(expected_persons, sorted_persons)


class Person:
    class ComparisonMode(Enum):
        FIRST_NAME = 0
        LAST_NAME = 1
        BOTH_NAMES = 2

    comparison_mode = ComparisonMode.BOTH_NAMES

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __comparison_key(self):
        if Person.comparison_mode == Person.ComparisonMode.FIRST_NAME:
            return self.first_name
        elif Person.comparison_mode == Person.ComparisonMode.LAST_NAME:
            return self.last_name
        else:
            return self.first_name, self.last_name

    def __eq__(self, other):
        return self.__comparison_key() == other.__comparison_key()

    def __ne__(self, other):
        return self.__comparison_key() != other.__comparison_key()

    def __lt__(self, other):
        return self.__comparison_key() < other.__comparison_key()

    def __le__(self, other):
        return self.__comparison_key() <= other.__comparison_key()

    def __gt__(self, other):
        return self.__comparison_key() > other.__comparison_key()

    def __ge__(self, other):
        return self.__comparison_key() >= other.__comparison_key()

    def __repr__(self):
        return "%s %s" % (self.first_name, self.last_name)

if __name__ == '__main__':
    unittest.main()
