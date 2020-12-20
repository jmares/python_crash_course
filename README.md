# Python Crash Course (2nd Ed)

A Hands-On, Project-Based Introduction to Programming by Eric Matthes   
Published by **no starch press** on May 2019, 544 pp.   
ISBN-13: 9781593279288

Started reading/studying this book on December 14, 2020.

This repo contains the exercises and examples of the book.

## PART I: Basics

### Chapter 01: Getting Started

December 14, 2020

Nothing new here for me, but used the example to famaliarize myself with Geany.

### Chapter 02: Variables and Simple Data Types

December 15, 2020

I already knew most of it, except the use of underscores in long numbers and multiple assignment.

```python
# use of underscores in long numbers
long_number = 14_000_000_000
print(long_number)
*14000000000*

# multiple assignment
x, y, z = 1, 2, 3

# convention for constants (python doens't have build in constant types)
MAX_CONNECTIONS = 5000
```

To find the **Zen of Python**

```python
import this
```

Only used the REPL for some of the examples.

### Chapter 03: Introducing Lists

December 20, 2020

Only used the REPL for some exercises.

How to get the last element of a list without knowing its length?

```python
last_item = my_list[-1]
```

Adding an item to the end of a list with `.append()`.

Inserting an item into a list with `.insert(position)`.

Removing an item from a list without returning its value with `del mylist(position)`.

Removing an item from a list and returning its value with `mylist.pop(position)`.

Removing an item by value with `mylist.remove('value')`.

Sorting a list permanently with `mylist.sort()` or `mylist.sort(reverse=True)`.

Sorting a list temporarily with `sorted(mylist)` or `sorted(mylist, reverse=True)`.

Reversing the order of a list with `mylist.reverse()`.

Finding the length of a list with `len(mylist)`.


### Chapter 04: Working with Lists

December 20, 2020

Only used the REPL for some exercises.

```python
numbers = list(range(2, 12, 2))
print(numbers)
# [2, 4, 6, 8, 10]
```

List comprehension

```python
squares = [value**2 for value in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Tuple = immutable list.

```python
my_list = [1, 2, 3, 4, 5]
my_tuple = [1, 2, 3, 4, 5]
```


### Chapter 05: if Statements

### Chapter 06: Dictionaries

### Chapter 07: User Input and while Loops

### Chapter 08: Functions

### Chapter 09: Classes

### Chapter 10: Files and Exceptions

### Chapter 11: Testing Your Code