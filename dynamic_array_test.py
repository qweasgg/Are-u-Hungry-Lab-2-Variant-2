import unittest
from hypothesis import given,  strategies

from dynamic_array import DynamicArray


class TestDynamicArray(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(DynamicArray().hello(), "hello")

    @given(strategies.integers(), strategies.integers())
    def test_add_commutative(self, a, b):
        self.assertEqual(DynamicArray().add(a, b), DynamicArray().add(b, a))
