from typing import Callable, List, Optional, TypeVar, Generic, Iterator

T = TypeVar('T')


class DynamicArray(Generic[T]):

    def __init__(self, initial_capacity: int = 10,
                 growth_factor: int = 2) -> None:
        self.capacity = initial_capacity
        self.growth_factor = growth_factor
        self.length = 0
        self.data: List[Optional[T]] = [None] * initial_capacity

    def __getitem__(self, index: int) -> Optional[T]:
        if 0 <= index < self.length:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index: int, value: T) -> None:
        if 0 <= index < self.length:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def __iter__(self) -> 'DynamicArray.DynamicArrayIterator[T]':
        return self.DynamicArrayIterator(self)

    class DynamicArrayIterator(Iterator[Optional[T]]):
        def __init__(self, dynamic_array: 'DynamicArray[T]') -> None:
            self._dynamic_array = dynamic_array
            self._index = 0

        def __next__(self) -> Optional[T]:
            if self._index < self._dynamic_array.length:
                value = self._dynamic_array[self._index]
                self._index += 1
                return value
            else:
                raise StopIteration

    def __eq__(self, other: object) -> bool:
        if isinstance(other, DynamicArray):
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
        new_data: List[Optional[T]] = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value: Optional[T]) -> None:
        if self.length == self.capacity:
            self._resize()
        self.data[self.length] = value
        self.length += 1


def cons(
        value: Optional[T],
        dynamic_array: Optional[DynamicArray[T]]
        ) -> DynamicArray[T]:
    cons_array = DynamicArray[T]()
    cons_array.append(value)
    if dynamic_array is not None:
        for item in dynamic_array:
            cons_array.append(item)
    return cons_array


def remove(
        dynamic_array: Optional[DynamicArray[T]],
        value: Optional[T]
        ) -> DynamicArray[T]:
    if dynamic_array is None:
        return DynamicArray[T]()
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    if v == value:
        return from_list(lst)
    return cons(v, remove(from_list(lst), value))


def size(dynamic_array: Optional[DynamicArray[T]]) -> int:
    if dynamic_array is None or dynamic_array.length == 0:
        return 0
    return dynamic_array.length


def is_member(dynamic_array: Optional[DynamicArray[T]], value: T) -> bool:
    if dynamic_array is None or size(dynamic_array) == 0:
        return False
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    if v == value:
        return True
    return is_member(from_list(lst), value)


def reverse(dynamic_array: Optional[DynamicArray[T]]) -> DynamicArray[T]:
    if dynamic_array is None or size(dynamic_array) == 0:
        return DynamicArray[T]()
    lst = to_list(dynamic_array)
    v = lst[len(lst) - 1]
    return cons(v, reverse(from_list(lst[0:(len(lst) - 1)])))


def intersection(
        instance1: Optional[DynamicArray[T]],
        instance2: Optional[DynamicArray[T]]
        ) -> bool:
    if size(instance1) == 0 or size(instance2) == 0:
        return False
    if instance1 is None or instance2 is None:
        return False
    lst = to_list(instance1)
    v = lst.pop(0)
    if v in instance2.data:
        return True
    return intersection(from_list(lst), instance2)


def to_list(dynamic_array: DynamicArray[T]) -> List[Optional[T]]:
    res: list[Optional[T]] = []

    def builder(array: DynamicArray[T]) -> List[Optional[T]]:
        if (size(array) == 0):
            return res
        v = array.data[0]
        if v is not None:
            res.append(v)
        else:
            res.append(None)
        rest_arr = from_list(array.data[1:size(array)])
        return builder(rest_arr)

    return builder(dynamic_array)


def from_list(lst: List[Optional[T]]) -> DynamicArray[T]:
    if len(lst) == 0:
        return DynamicArray[T]()
    return cons(lst[0], from_list(lst[1:]))


def find(
        dynamic_array: DynamicArray[T],
        predicate: Callable[[T], T]
        ) -> Optional[T]:
    if dynamic_array is None or (size(dynamic_array) == 0):
        return None
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    if v is not None:
        if predicate(v):
            return v
    return find(from_list(lst), predicate)


def filter(dynamic_array: DynamicArray[T],
           func: Callable[[T], T]
           ) -> DynamicArray[T]:
    if dynamic_array is None or (size(dynamic_array) == 0):
        return DynamicArray[T]()
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    if v is not None:
        if func(v):
            return cons(v, filter(from_list(lst), func))
    return filter(from_list(lst), func)


def map(
        dynamic_array: DynamicArray[T],
        func: Callable[..., T]
        ) -> DynamicArray[T]:
    if dynamic_array is None or (size(dynamic_array) == 0):
        return DynamicArray[T]()
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    return cons(func(v), map(from_list(lst), func))


def reduce(dynamic_array: Optional[DynamicArray[T]],
           func: Callable[..., T], value: T) -> T:
    if dynamic_array is None or (size(dynamic_array) == 0):
        return value
    lst = to_list(dynamic_array)
    v = lst.pop(0)
    value = func(value, v)
    return reduce(from_list(lst), func, value)


def iterator(
        dynamic_array: Optional[DynamicArray[T]]
        ) -> Callable[[], Optional[T]]:
    if dynamic_array is None:
        raise StopIteration
    lst = dynamic_array
    len = size(lst)
    i = 0

    def foo() -> Optional[T]:
        nonlocal lst
        nonlocal len
        nonlocal i
        if i >= len:
            raise StopIteration
        tmp = lst.data[i]
        i += 1
        return tmp

    return foo


def empty() -> DynamicArray[T]:
    array = DynamicArray[T]()
    return array


def concat(
        instance1: Optional[DynamicArray[T]],
        instance2: Optional[DynamicArray[T]]
        ) -> Optional[DynamicArray[T]]:
    if instance1 is None or (size(instance1) == 0):
        return instance2
    if instance2 is None or (size(instance2) == 0):
        return instance1
    lst = to_list(instance1)
    v = lst[len(lst) - 1]
    new_i2 = cons(v, instance2)
    return concat(from_list(lst[0:len(lst) - 1]), new_i2)
