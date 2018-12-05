import sys
import unittest
from unittest import TestCase

from qsort import qsort

# https://docs.python.org/3/library/unittest.html


class TestQsort(TestCase):
    def test_qsort(self):
        self.fail()

    def test_qsort_when_empty_then_empty(self):
        empty_result = qsort.qsort([])
        self.assertIsNotNone(empty_result, "empty array should not return None")
        self.assertTrue(len(empty_result) == 0)

    def test_qsort_when_none_then_empty(self):
        empty_result = qsort.qsort(None)
        self.assertIsNotNone(empty_result, "None should not return None")
        self.assertTrue(len(empty_result) == 0)

    def test_qsort_when_one_then_one(self):
        one_result = qsort.qsort([1])
        self.assertTrue(len(one_result) == 1)
        self.assertEqual(one_result[0], 1)

    def test_qsort_when_two(self):
        arr = [2, 1]
        two_result = qsort.qsort(arr)
        self.assertEqual(two_result, [1, 2])

    def test_qsort_when_two(self):
        arr = list(range(10, 0, -1))
        result = qsort.qsort(arr)
        self.assertEqual(result, list(range(1, 11)))

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    # @unittest.skipIf(mylib.__version__ < (1, 3),
    #                  "not supported in this library version")
    # def test_format(self):
    #     # Tests that work for only a certain version of the library.
    #     pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

    def tearDown(self):
        pass

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def setUpClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
