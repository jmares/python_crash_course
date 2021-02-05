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

January 04, 2021

### Chapter 06: Dictionaries

January 05, 2021

Must of this stuff is beginner's stuff, which I already know. But I have found two usefull bits of information:

First: 

"As of Python 3.7, dictionaries retain the order in which they were defined."

Second:

Suppose you have a dictionary with names (*keys*) of people and their favorite programming language (*values*). 
You want to display a list of the unique programming languages: get a list with the values of the dictionary using the `values()` method and use the `set()` function to return a collection with unique items.

```python
for language in set(favorite_languages.values()):
    print(language)
```


### Chapter 07: User Input and while Loops

January 6, 2021

Whenever I needed input from a user, I always used a short, clear, easy-to-understand prompt. It never occured to me that I could use a multi-line string.


### Chapter 08: Functions

January 7, 2021

Paramaters and username: `username` is the parameter and `'Jessie'` is the argument.

```python
def greet_user(username):
    #some code

greet_user('Jessie')
```

Positional arguments, default values and keyword arguments:

```python
def describe_pet(pet_name, animal_type = 'dog'):
    #some code

describe_pet('Willie')
describe_pet('Harry', 'hamster')
describe(animal_type='cat', pet_name='Tiger')
```

When you pass a list to a function and modify the list inside the function, the original list gets modified.
When you don't want that, you have to pass a copy of the list to the function.

```python
def mod_list(lst):
    #some code

a = ['a', 'b', 'c', 'd', 'e']
mod_list(a[:])
```

An arbitrary number of arguments

```python
def make_pizza(size='large', *toppings):
    #some code
    # toppings is a list
    #some code

make_pizza('small', 'mushrooms', 'green pepers', 'extra cheese')
```

An arbitrary number of keyword arguments

```python
def build_profile(first, last, **user_info):
    #some code
    # user_info is a dictionary
    #some code

build_profile('John', 'Doe', location='New York', profession='waiter', age=42)
```

Putting functions in a separate file (*module*) and import them

```python
import module_name # without the .py, import everything

module_name.function_name()

from module_name import function_0, function_1, function_2 # import only specific functions

function_0()

from module_name import function_name as funa # import specific function and give it an alias

funa()

import module_name as mn # import everything, give module an alias

mn.function_name()

from module_name import * # import every function
```

- Function names in python: descriptive, use lowercase letters and underscores.
- Dito for modules.
- Default value: no spaces on either side of the equal sign.
- Dito for keyword arguments
- Separate functions by two empty lines
- All import statements should be at the beginning of a file
- Document function using docstring format `""" comment """`

### Chapter 09: Classes

January 8, 2021

### Chapter 10: Files and Exceptions

January 10, 2021

Had not encountered an `else` block in a `try-except` before.

```python
try:
    # code that can cause an error belongs here
except:
    # what to do when an exception occurs
else:
    # do this when no exception occured
```

The `pass` statement: do nothing.

Refactoring makes code cleaner, easier to understand, and easier to extend.
Improving code by breaking it up into a series of functions that have specific jobs, is called *refactoring*.

### Chapter 11: Testing Your Code

January 11, 2021

Which book is best to start studying python? This one or "*Python for Everybody*" by Charles Severance?   
Difficult choice, but the inclusion of unittesting in this book is a bonus.

## PART II: Projects

## Project 1: Alien Invasion

### Chapter 12: A Ship that Fires Bullets

January 12 - 13, 2021

### Chapter 13: Aliens!

January 14 - 15, 2021

I am not interested in developing games and intended to go through these chapters quickly.

The way you program this game and use the library forces me think about programming in a different way.
I am going to focus on working with, but I will revisit this in the future.

### Chapter 14: Scoring

January 16 - 17, 2021

## Project 2: Data Visualization

### Chapter 15: Generating Data

January 18 - 20, 2021

### Chapter 16: Downloading Data

January 21 - 22, 2021

### Chapter 17: Working with APIs

January 23 - 24, 2021

I encountered only a couple of bugs in this book so far, but haven't documented them.

One encountered in this chapter was with the Hacker News code: it didn't take into account that a keyword could be missing, eg. an article without comments has no 'descendants.

Code in the book for `hn_submissions.py`:

```python
submission_dict = {
    'title': response_dict['title'],
    'hn_link': f"http://news.ycombinator.com/item?id={ submission_id }",
    'comments': response_dict['descendants'],
}
```

which resulted in the following error:

```bash
Traceback (most recent call last):
  File ".\hn_submissions.py", line 25, in <module>
    'comments': response_dict['descendants'],
KeyError: 'descendants'
```

Solution:

```python
submission_dict = {
    'title': response_dict['title'],
    'hn_link': f"http://news.ycombinator.com/item?id={ submission_id }",
    'comments': response_dict.get('descendants', 0),
}
```

## Project 3: Web Applications

### Chapter 18: Getting Started with Django

January 25 - 26, 2021

All code in folder `learning_log`

### Chapter 19: User Accounts

January 28 - 29, 2021

All code in folder `learning_log`

### Chapter 20: Styling and Deploying an App

January 30 - 31, 2021

All code in folder `learning_log`

When setting DEBUG based on environment variables, I got an error when pushing the code to heroku: 

```bash
 NameError: name 'os' is not defined
```

In the code sample `os` was not imported. Correct code:

```python
# Heroku settings
import django_heroku, os
django_heroku.settings(locals())

if os.environ.get('DEBUG') == 'TRUE':
    DEBUG = True
elif os.environ.get('DEBUG') == 'FALSE':
    Debug = False
```

Didn't get the custom error pages to work. Don't know whether it is caused by a typo of mine, an error in the code, ..., but as I have no immediate plans to use Django I left it at that.
