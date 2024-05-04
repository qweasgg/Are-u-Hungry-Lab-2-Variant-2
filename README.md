# Are u Hungry - lab 2 - variant 2

  This project implements a dynamic array data structure in Python.
  A dynamic array is a resizable array that grows in size when an element is appended.

## Project structure

- `dynamic_array.py` -- implementation of `DynamicArray` class with some features.

- `dynamic_array_test.py` -- unit tests for `DynamicArray`.

## Features

- Dynamic resizing: The dynamic array can automatically expand as needed.
- Index operations: Support accessing and setting elements by index.
- Data manipulation: Implement common array functionalities and
  support operations like filtering and mapping.
- Unit testing: Includes a comprehensive unit test suite.

## Contribution

- Yang Ao (1031901332@qq.com) -- source code.
- Ying Yi (1812742922@qq.com) -- PBT test.

## Changelog

- 04.05.2024 - 6
  Add strict for mypy
  Compare the differences between mut and immut

- 26.04.2024 - 5
  Add test_api in the PBT test
  Modify some implement to receive imput None

- 26.04.2024 - 4
  Modify PBT test

- 25.04.2024 - 3
  Modify some features implement

- 21.04.2024 - 2
  Write the PBT test for all features
  Modify some features implement
  Reformat the whole code

- 21.04.2024 - 1
  Write the source code for implementation

- 20.04.2024 - 0
  Initialize and write README
  Set black . to complete code formatting

## Design notes

- Create a Class called DynamicArray to implement the task. In the dynamic
  array implementation, I used a fixed-size built-in list to store elements
  which helps improve memory efficiency.

- We allow users to specify the initial capacity and growth factor, enabling
  them to adjust the performance and memory usage of the dynamic array
  according to their actual needs.

- The core functionalities include: accessing and setting elements by index,
  dynamically resizing the array, removing specific element, reverse the array,
  iterating over the array, and utilizing filter and map operations.

- Our implementation also ensures proper handling of None values.
  When the input is None, the program will prompt an error.

## Comparison

- Using mutable methods allows us to directly modify data structures, providing
high flexibility and potentially reducing memory overhead. However, mutable data
structures may lead to code that is difficult to understand and can result in
race conditions and synchronization issues in multi-threaded environments.

- Using immutable methods prevents direct modification of the original data structure,
making it inherently thread-safe and simplifying concurrent programming 
but may have lower efficiency.

- In general, we should choose the appropriate method based on practical considerations. 
