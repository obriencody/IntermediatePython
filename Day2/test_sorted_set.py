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
        self.assertFalse(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)

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

class TestIterableProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([7, 2, 1, 1, 9])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 7)
        self.assertEqual(next(i), 9)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_for_loop(self):
        index = 0
        expected = [1, 2, 7, 9]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1

class TestSequenceProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([1, 4, 9, 13, 15])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_four(self):
        self.assertEqual(self.s[4], 15)

    def test_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.s[5]

    def test_index_minus(self):
        self.assertEqual(self.s[-1], 15)

    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)

    def test_minus_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.s[-6]

    # Slicing
    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1, 4, 9]))

    def test_slice_from_end(self):
        self.assertEqual(self.s[3:], SortedSet([13, 15]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet())

    def test_slice_arbitrary(self):
        self.assertEqual(self.s[2:4], SortedSet([9, 13]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)

class TestReportProtocol(unittest.TestCase):
    def test_report_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet()")

    def test_report_some(self):
        s = SortedSet([42, 40, 19])
        self.assertEqual(repr(s), "SortedSet([19, 40, 42])")

class TestEqualityProtocol(unittest.TestCase):
    def test_positive_equal(self):
        self.assertTrue(SortedSet([1, 2, 3]) == SortedSet([1, 2, 3]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([1, 2, 3]) == SortedSet([4, 5, 6]))

    def test_mismatch(self):
        self.assertFalse(SortedSet([1, 2, 3]) == [1, 2, 3])

    def test_identical(self):
        s = SortedSet([1, 2, 3])
        self.assertTrue(s == s)

    def test_positive_unequal(self):
        self.assertTrue(SortedSet([1, 2, 3]) != SortedSet([4, 5, 6]))

    def test_negative_unequal(self):
        self.assertFalse(SortedSet([1, 2, 3]) != SortedSet([3, 2, 1]))

    def test_mismatch_unequal(self):
        self.assertTrue(SortedSet([1, 2, 3]) != [1, 2, 3])

    def test_identical_unequal(self):
        s = SortedSet([1, 2, 3])
        self.assertFalse(s != s)


if __name__ == '__main__':
    unittest.main()
