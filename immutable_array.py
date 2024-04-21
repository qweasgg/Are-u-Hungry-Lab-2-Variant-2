class DynamicArray(object):

    def __init__(self, initial_capacity=10, growth_factor=2):
        self.capacity = initial_capacity
        self.growth_factor = growth_factor
        self.length = 0
        self.data = [None] * initial_capacity

    def __getitem__(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < self.length:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < self.length:
            value = self.data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

    def __eq__(self, other):
        if self.length != other.length:
            return False
        for i in range(self.length):
            if self.data[i] != other.data[i]:
                return False
        return True

    def __str__(self):
        return "[" + ", ".join(str(item) for item in self) + "]"

    def _resize(self):
        new_capacity = self.capacity * self.growth_factor
        new_data = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if value is None:
            raise ValueError("Input is None")
        if self.length == self.capacity:
            self._resize()
        self.data[self.length] = value
        self.length += 1


def cons(dynamic_array: DynamicArray, value):
    cons_array = DynamicArray()
    for item in dynamic_array:
        cons_array.append(item)
    cons_array.append(value)
    return cons_array


def remove(dynamic_array: DynamicArray, value):
    removed_array = DynamicArray()
    index = -1
    for i in range(dynamic_array.length):
        if dynamic_array.data[i] == value:
            index = i
        else:
            removed_array.append(dynamic_array.data[i])
    if index >= 0:
        return removed_array
    else:
        return ValueError("Value not found")


def size(dynamic_array: DynamicArray):
    return dynamic_array.length


def is_member(dynamic_array: DynamicArray, value):
    for i in range(dynamic_array.length):
        if dynamic_array.data[i] == value:
            return i
    return -1


def reverse(dynamic_array: DynamicArray):
    reserved_array = DynamicArray()
    size = dynamic_array.length
    for i in range(dynamic_array.length):
        reserved_array.append(dynamic_array.data[size - i - 1])
    return reserved_array


def intersection(instance1: DynamicArray, instance2: DynamicArray):
    intersected_array = DynamicArray()
    for item in instance1:
        if item in instance2 and item not in intersected_array:
            intersected_array.append(item)
    return intersected_array


def to_list(dynamic_array: DynamicArray):
    return [item for item in dynamic_array]


def from_list(lst):
    dynamic_array = DynamicArray()
    for item in lst:
        dynamic_array.append(item)
    return dynamic_array


def find(dynamic_array: DynamicArray, predicate):
    for item in dynamic_array:
        if predicate(item):
            return item
    return None


def filter(dynamic_array: DynamicArray, filter):
    filter_array = DynamicArray()
    for item in dynamic_array:
        if filter(item):
            filter_array.append(item)
    return filter_array


def map(dynamic_array: DynamicArray, function):
    map_array = DynamicArray()
    for item in dynamic_array:
        map_array.append(function(item))
    return map_array


def reduce(dynamic_array: DynamicArray, function):
    value = dynamic_array.data[0]
    for i in range(dynamic_array.length):
        if i == 0:
            continue
        value = function(value, dynamic_array.data[i])
    return value


def iterator(dynamic_array: DynamicArray):
    return dynamic_array.__iter__()


def empty():
    array = DynamicArray()
    return array


def concat(instance1: DynamicArray, instance2: DynamicArray):
    concat_array = DynamicArray()
    for item in instance1:
        concat_array.append(item)
    for item in instance2:
        concat_array.append(item)
    return concat_array
