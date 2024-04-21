import unittest
from hypothesis import given, strategies

from immutable_array import DynamicArray, cons, remove, size, is_member
from immutable_array import reverse, intersection, to_list, from_list, find
from immutable_array import filter, map, reduce, iterator, concat, empty


class TestDynamicArray(unittest.TestCase):

    @given(strategies.integers())
    def test_cons(self, v):
        array1 = DynamicArray()
        array2 = cons(array1, v)
        self.assertEqual(array2.length, 1)
        self.assertEqual(array2.data[0], v)

    @given(strategies.integers())
    def test_remove(self, v1):
        array = DynamicArray()
        array = cons(array, v1)
        removed_array = remove(array, v1)
        self.assertEqual(removed_array.length, 0)

    @given(strategies.integers(), strategies.integers())
    def test_size(self, v1, v2):
        array = DynamicArray()
        self.assertEqual(size(array), 0)
        array = cons(array, v1)
        array = cons(array, v2)
        self.assertEqual(size(array), 2)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_is_member(self, v1, v2, v3):
        array = DynamicArray()
        array = cons(array, v1)
        array = cons(array, v2)
        array = cons(array, v3)
        index = is_member(array, v1)
        self.assertEqual(index, 0)
        array = remove(array, v3)
        index = is_member(array, v3)
        self.assertEqual(index, -1)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_reverse(self, v1, v2, v3):
        array = DynamicArray()
        array = cons(array, v1)
        array = cons(array, v2)
        array = cons(array, v3)
        array = reverse(array)
        self.assertEqual(array.data[0], v3)
        self.assertEqual(array.data[2], v1)

    @given(strategies.integers(), strategies.integers())
    def test_intersection(self, v1, v2):
        array1 = DynamicArray()
        array1 = cons(array1, v1)
        array1 = cons(array1, v2)
        array2 = DynamicArray()
        array2 = cons(array2, v1)
        intersection_array = intersection(array1, array2)
        self.assertEqual(intersection_array.length, 1)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_to_list(self, v1, v2, v3):
        array = DynamicArray()
        lst = [v1, v2, v3]
        array = cons(array, v1)
        array = cons(array, v2)
        array = cons(array, v3)
        self.assertEqual(to_list(array), lst)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_from_list(self, v1, v2, v3):
        array = DynamicArray()
        lst = [v1, v2, v3]
        array = from_list(lst)
        self.assertEqual(array.length, 3)

    def test_filter(self):
        def is_even(num):
            return num % 2 == 0

        array = DynamicArray()
        lst = [1, 2, 3]
        array = from_list(lst)
        even_array = filter(array, is_even)
        self.assertEqual(even_array.length, 1)

    def test_find(self):
        def is_even(num):
            return num % 2 == 0

        array = DynamicArray()
        lst = [2, 4, 6]
        array = from_list(lst)
        value = find(array, is_even)
        self.assertEqual(value, 2)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_map(self, v1, v2, v3):
        def increment(num):
            return num + 1

        array = DynamicArray()
        lst = [v1, v2, v3]
        array = from_list(lst)
        array = map(array, increment)
        self.assertEqual(array.data[1], v2 + 1)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_reduce(self, v1, v2, v3):
        def sum(num1, num2):
            return num1 + num2

        array = DynamicArray()
        lst = [v1, v2, v3]
        array = from_list(lst)
        value = reduce(array, sum)
        self.assertEqual(value, v1 + v2 + v3)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_iterator(self, v1, v2, v3):
        array = DynamicArray()
        lst = [v1, v2, v3]
        array = from_list(lst)
        i = iterator(array)
        self.assertEqual(i.__next__(), v1)
        self.assertEqual(i.__next__(), v2)
        self.assertEqual(i.__next__(), v3)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_concat(self, v1, v2, v3):
        lst = [v1]
        a = from_list(lst)
        lst = [v2]
        b = from_list(lst)
        lst = [v3]
        c = from_list(lst)
        lst1 = to_list(concat(a, concat(b, c)))
        lst2 = to_list(concat(concat(a, b), c))
        self.assertEqual(lst1, lst2)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_empty(self, v1, v2, v3):
        e = empty()
        lst = [v1, v2, v3]
        array = from_list(lst)
        lst1 = to_list(concat(e, array))
        lst2 = to_list(concat(array, e))
        self.assertEqual(lst, lst1)
        self.assertEqual(lst1, lst2)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_eq(self, v1, v2, v3):
        e = empty()
        lst = [v1, v2, v3]
        a = from_list(lst)
        a1 = concat(a, e)
        a2 = concat(e, a)
        self.assertEqual(a1, a2)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_str(self, v1, v2, v3):
        lst = [v1, v2, v3]
        a1 = from_list(lst)
        s1 = a1.__str__()
        s2 = lst.__str__()
        self.assertEqual(s1, s2)
