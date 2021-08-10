import unittest
from sorted_set import SortedSet

class TestConstructor(unittest.TestCase):
    def test_empty(self):
        s = SortedSet([])
        # self.assertEqual(True, False)  # add assertion here

    def test_sequence(self):
        s = SortedSet([7, 8, 3, 1])

    def test_duplicates(self):
        s = SortedSet([7, 8, 8, 7])

    def test_from_iterables(self):
        def gen6842():
            yield 6
            yield 8
            yield 4
            yield 2

        g = gen6842()
        s = SortedSet(g)

class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([6, 7, 3, 9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertTrue(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)

    def test_negative_not_contained(self):
        self.assertTrue(9 not in self.s)

class TestSizeProtocol(unittest.TestCase):
    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([2])
        self.assertEqual(len(s), 1)

    def test_10(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_with_duplicates(self):
        s = SortedSet([5, 5, 5])
        self.assertEqual(len(s), 1)

if __name__ == '__main__':
    unittest.main()
