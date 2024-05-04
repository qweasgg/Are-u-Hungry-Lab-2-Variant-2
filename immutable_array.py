from typing import Any, List, Callable


class DynamicArray(object):

    def __init__(self, initial_capacity: int = 10,
                 growth_factor: int = 2) -> None:
        self.capacity = initial_capacity
        self.growth_factor = growth_factor
        self.length = 0
        self.data = [None] * initial_capacity

    def __getitem__(self, index: Any) -> Any:
        if 0 <= index < self.length:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index: Any, value: Any) -> Any:
        if 0 <= index < self.length:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def __iter__(self) -> Any:
        self._index = 0
        return self

    def __next__(self) -> Any:
        if self._index < self.length:
            value = self.data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

    def __eq__(self, other: object) -> bool:
        if type(other) is DynamicArray:
            if self.length != other.length:
                return False
            for i in range(self.length):
                if self.data[i] != other.data[i]:
                    return False
            return True
        return False

    def __str__(self) -> str:
        return "[" + ", ".join(str(item) for item in self) + "]"

    def _resize(self) -> None:
        new_capacity = self.capacity * self.growth_factor
        new_data = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value: Any) -> None:
        if self.length == self.capacity:
            self._resize()
        self.data[self.length] = value
        self.length += 1


def cons(value: Any, dynamic_array: DynamicArray) -> DynamicArray:
    cons_array = DynamicArray()
    cons_array.append(value)
    if dynamic_array is None:
        return cons_array
    for item in dynamic_array:
        cons_array.append(item)
    return cons_array


def remove(dynamic_array: DynamicArray, value: Any) -> DynamicArray:
    if dynamic_array.length == 0:
        return DynamicArray()
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    if v == value:
        return from_list(lst)
    return cons(v, remove(from_list(lst), value))


def size(dynamic_array: DynamicArray) -> int:
    return dynamic_array.length


def is_member(dynamic_array: DynamicArray, value: Any) -> bool:
    if size(dynamic_array) == 0:
        return False
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    if v == value:
        return True
    return is_member(from_list(lst), value)


def reverse(dynamic_array: DynamicArray) -> DynamicArray:
    if size(dynamic_array) == 0:
        return DynamicArray()
    lst = to_list(dynamic_array)
    v = lst[len(lst) - 1]
    return cons(v, reverse(from_list(lst[0:(len(lst) - 1)])))


def intersection(instance1: DynamicArray, instance2: DynamicArray) -> bool:
    if size(instance1) == 0 or size(instance2) == 0:
        return False
    lst = to_list(instance1)
    v = lst.pop(0)
    if v in instance2.data:
        return True
    return intersection(from_list(lst), instance2)


def to_list(dynamic_array: DynamicArray) -> List[Any]:
    res: list[type] = []

    def builder(array: Any) -> List[Any]:
        if size(array) == 0:
            return res
        v = array.data[0]
        rest_arr = from_list(array.data[1:size(array)])
        res.append(v)
        return builder(rest_arr)

    return builder(dynamic_array)


def from_list(lst: List[Any]) -> DynamicArray:
    if len(lst) == 0:
        return DynamicArray()
    return cons(lst[0], from_list(lst[1:]))


def find(dynamic_array: DynamicArray, predicate: Callable[[Any], Any]) -> Any:
    if size(dynamic_array) == 0:
        return None
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    if predicate(v):
        return v
    return find(from_list(lst), predicate)


def filter(dynamic_array: DynamicArray,
           func: Callable[[Any], Any]) -> DynamicArray:
    if size(dynamic_array) == 0:
        return DynamicArray()
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    if func(v):
        return cons(v, filter(from_list(lst), func))
    return filter(from_list(lst), func)


def map(dynamic_array: DynamicArray, func: Callable[..., Any]) -> DynamicArray:
    if size(dynamic_array) == 0:
        return DynamicArray()
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    return cons(func(v), map(from_list(lst), func))


def reduce(dynamic_array: DynamicArray,
           func: Callable[..., Any], value: Any) -> Any:
    if size(dynamic_array) == 0:
        return value
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    value = func(value, v)
    return reduce(from_list(lst), func, value)


def iterator(dynamic_array: DynamicArray) -> Any:
    if dynamic_array is None:
        raise StopIteration
    lst = dynamic_array
    len = size(lst)
    i = 0

    def foo() -> Any:
        nonlocal lst
        nonlocal len
        nonlocal i
        if i >= len:
            raise StopIteration
        tmp = lst.data[i]
        i += 1
        return tmp

    return foo


def empty() -> DynamicArray:
    array = DynamicArray()
    return array


def concat(instance1: DynamicArray, instance2: DynamicArray) -> DynamicArray:
    if size(instance1) == 0:
        return instance2
    if size(instance2) == 0:
        return instance1
    lst = to_list(instance1)
    v = lst[len(lst) - 1]
    new_i2 = cons(v, instance2)
    return concat(from_list(lst[0:len(lst) - 1]), new_i2)
