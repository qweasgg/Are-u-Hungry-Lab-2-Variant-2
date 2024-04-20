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

## Changelog

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
