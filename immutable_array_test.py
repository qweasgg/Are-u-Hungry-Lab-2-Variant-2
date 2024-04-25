import unittest
from hypothesis import given, strategies

from immutable_array import DynamicArray, cons, remove, size, is_member
from immutable_array import reverse, intersection, to_list, from_list, find
from immutable_array import filter, map, reduce, iterator, concat, empty


class TestDynamicArray(unittest.TestCase):

    @given(strategies.integers())
    def test_cons(self, v):
        lst = [1, 2, 3]
        array1 = from_list(lst)
        array2 = cons(v, array1)
        self.assertEqual(array2.length, 4)
        self.assertEqual(array2.data[0], v)
        self.assertEqual(to_list(array2), [v, 1, 2, 3])

    @given(strategies.integers())
    def test_remove(self, v):
        lst = [1, 2, 3]
        array = from_list(lst)
        removed_array = remove(array, 2)
        self.assertEqual(removed_array.length, 2)

    @given(strategies.integers(), strategies.integers())
    def test_size(self, v1, v2):
        lst = [1, 2, 3]
        array = from_list(lst)
        self.assertEqual(size(array), 3)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_is_member(self, v1, v2, v3):
        lst = [1, 2, 3]
        array = from_list(lst)
        self.assertEqual(is_member(array, 2), True)
        self.assertEqual(is_member(array, 0), False)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_reverse(self, v1, v2, v3):
        lst = [1, 2, 3]
        array = from_list(lst)
        self.assertEqual(to_list(reverse(array)), [3, 2, 1])

    @given(strategies.integers(), strategies.integers())
    def test_intersection(self, v1, v2):
        lst = [1, 2, 3]
        array1 = from_list(lst)
        lst = [2, 3, 4]
        array2 = from_list(lst)
        lst = [0]
        array3 = from_list(lst)
        self.assertEqual(intersection(array1, array2), True)
        self.assertEqual(intersection(array1, array3), False)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_to_list(self, v1, v2, v3):
        lst = [1, 2, 3]
        array = from_list(lst)
        self.assertEqual(to_list(array), lst)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_from_list(self, v1, v2, v3):
        lst = [1, 2, 3]
        array = from_list(lst)
        self.assertEqual(to_list(array), lst)

    def test_find(self):
        def is_even(num):
            return num % 2 == 0

        lst = [1, 2, 4, 6]
        array = from_list(lst)
        value = find(array, is_even)
        self.assertEqual(value, 2)

    def test_filter(self):
        def is_even(num):
            return num % 2 == 0

        lst = [1, 2, 3, 4]
        array = from_list(lst)
        self.assertEqual(to_list(filter(array, is_even)), [2, 4])

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_map(self, v1, v2, v3):
        def increment(num):
            return num + 1

        lst = [1, 2, 3]
        array = from_list(lst)
        self.assertEqual(to_list(map(array, increment)), [2, 3, 4])

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_reduce(self, v1, v2, v3):
        def sum(num1, num2):
            return num1 + num2

        lst = [1, 2, 3, 4]
        array = from_list(lst)
        self.assertEqual(reduce(array, sum, 0), 10)

    @given(strategies.integers(), strategies.integers(), strategies.integers())
    def test_iterator(self, v1, v2, v3):
        lst = [1, 2, 3]
        arr = from_list(lst)

        tmp = []
        try:
            get_next = iterator(arr)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(lst, tmp)
        self.assertEqual(to_list(arr), tmp)

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
        e = DynamicArray()
        lst = [1, 2, 3]
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
