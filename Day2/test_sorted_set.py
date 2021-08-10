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


if __name__ == '__main__':
    unittest.main()
