import unittest
from hypothesis import given,  strategies

from immutable_array import DynamicArray, cons


class TestDynamicArray(unittest.TestCase):

    @given(strategies.integers())
    def test_cons(self, v):
        array1 = DynamicArray()
        array2 = cons(array1, v)
        self.assertEqual(array2.length, 1)
        self.assertEqual(array2.data[0], v)
