# Algorithm Explorer & Complexity Analyzer

## Overview

Algorithm Explorer & Complexity Analyzer is a Python-based interactive project developed for CSE1021 – Problem Solving and Programming.

The project allows users to execute selected fundamental algorithms, observe their results, and understand their basic time and space complexity.

The project focuses on algorithms and programming concepts covered in the course rather than using advanced libraries or frameworks.

---

## Objectives

The main objectives of this project are:

- To implement fundamental algorithms using Python.
- To understand how algorithms work through practical execution.
- To demonstrate searching, sorting and recursion.
- To provide basic time and space complexity information.
- To practice input validation and modular programming.
- To test the implemented algorithms using different cases.

---

## Features

### 1. Search Lab

Implements Linear Search.

The user provides a list of numbers and a target value.

The program displays:

- Whether the target was found.
- Its position if found.
- Number of comparisons performed.

### 2. Sorting Lab

Implements Selection Sort.

The program displays:

- Original list.
- Sorted list.
- Number of comparisons.
- Number of swaps.

### 3. Recursion Lab

Demonstrates three recursive algorithms:

- Factorial
- Fibonacci
- Tower of Hanoi

### 4. Complexity Analyzer

Provides basic complexity information for the implemented algorithms, including:

- Best case
- Worst case
- Space complexity
- Short explanation

### 5. Input Validation

The project validates user input and handles invalid values such as:

- Non-integer input
- Empty number lists
- Negative values where not allowed

### 6. Testing

A separate test file is included to check the main algorithm implementations.

---

## Technologies Used

- Python 3
- Python Standard Library
- VS Code
- Git
- GitHub

No external Python packages are required.

---

## Project Structure

```text
Algorithm-Explorer/
│
├── main.py
│
├── modules/
│   ├── __init__.py
│   ├── search.py
│   ├── sorting.py
│   ├── recursion.py
│   ├── complexity.py
│   └── validation.py
│
├── tests/
│   └── test_algorithms.py
│
├── docs/
│
├── README.md
├── statement.md
