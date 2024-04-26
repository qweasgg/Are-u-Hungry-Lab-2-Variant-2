import unittest
from hypothesis import given, strategies

from immutable_array import cons, remove, size, is_member
from immutable_array import reverse, intersection, to_list, from_list, find
from immutable_array import filter, map, reduce, iterator, concat, empty


class TestDynamicArray(unittest.TestCase):

    @given(strategies.lists(strategies.integers()), strategies.integers())
    def test_cons(self, lst, v):
        dynamic_array = from_list(lst)
        lst.insert(0, v)
        cons_array = cons(v, dynamic_array)
        self.assertEqual(to_list(cons_array), lst)

    @given(strategies.lists(strategies.integers()), strategies.integers())
    def test_remove(self, lst, v):
        dynamic_array = from_list(lst)
        cons_array = cons(v, dynamic_array)
        remove_array = remove(cons_array, v)
        self.assertEqual(to_list(remove_array), lst)

    @given(strategies.lists(strategies.integers()))
    def test_size(self, lst):
        dynamic_array = from_list(lst)
        self.assertEqual(size(dynamic_array), len(lst))

    def test_is_member(self):
        lst = [1, 2, 3]
        dynamic_array = from_list(lst)
        self.assertEqual(is_member(dynamic_array, 2), True)
        self.assertEqual(is_member(dynamic_array, 0), False)

    @given(strategies.lists(strategies.integers()))
    def test_reverse(self, lst):
        dynamic_array = from_list(lst)
        lst.reverse()
        reverse_array = reverse(dynamic_array)
        self.assertEqual(reverse_array, from_list(lst))

    @given(
        strategies.lists(strategies.integers()),
        strategies.lists(strategies.integers()),
        strategies.integers(),
    )
    def test_intersection(self, lst1, lst2, v):
        array1 = cons(v, from_list(lst1))
        array2 = cons(v, from_list(lst2))
        array3 = empty()
        self.assertEqual(intersection(array1, array2), True)
        self.assertEqual(intersection(array1, array3), False)

    @given(strategies.lists(strategies.integers()))
    def test_to_list(self, lst):
        dynamic_array = from_list(lst)
        self.assertEqual(to_list(dynamic_array), lst)

    @given(strategies.lists(strategies.integers()))
    def test_from_list(self, lst):
        dynamic_array = from_list(lst)
        self.assertEqual(to_list(dynamic_array), lst)

    @given(strategies.lists(strategies.integers()))
    def test_find(self, lst):
        def is_even(num):
            return num % 2 == 0

        dynamic_array = from_list(lst)
        value = find(cons(2, dynamic_array), is_even)
        self.assertEqual(value, 2)

    @given(strategies.lists(strategies.integers()))
    def test_filter(self, lst):
        def is_even(num):
            return num % 2 == 0

        dynamic_array = from_list(lst)
        filter_array = filter(dynamic_array, is_even)
        filter_list = [x for x in lst if is_even(x)]
        self.assertEqual(to_list(filter_array), filter_list)

    @given(strategies.lists(strategies.integers()))
    def test_map(self, lst):
        def increment(num):
            return num + 1

        map_list = [x + 1 for x in lst]
        dynamic_array = from_list(lst)
        map_array = map(dynamic_array, increment)
        self.assertEqual(to_list(map_array), map_list)

    @given(strategies.lists(strategies.integers()))
    def test_reduce(self, lst):
        def sum(num1, num2):
            return num1 + num2

        total = 0
        for num in lst:
            total += num
        dynamic_array = from_list(lst)
        self.assertEqual(reduce(dynamic_array, sum, 0), total)

    @given(strategies.lists(strategies.integers()))
    def test_iterator(self, lst):
        dynamic_array = from_list(lst)
        tmp = []
        try:
            get_next = iterator(dynamic_array)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(lst, tmp)
        self.assertEqual(to_list(dynamic_array), tmp)

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

    @given(strategies.lists(strategies.integers()))
    def test_empty(self, lst):
        e = empty()
        a = from_list(lst)
        lst1 = to_list(concat(e, a))
        lst2 = to_list(concat(a, e))
        self.assertEqual(lst, lst1)
        self.assertEqual(lst1, lst2)

    @given(strategies.lists(strategies.integers()))
    def test_eq(self, lst):
        e = empty()
        a = from_list(lst)
        self.assertEqual(concat(e, a), concat(a, e))

    @given(strategies.lists(strategies.integers()))
    def test_str(self, lst):
        dynamic_array = from_list(lst)
        self.assertEqual(dynamic_array.__str__(), lst.__str__())
