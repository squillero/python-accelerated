---
theme : "night"
transition: "slide"
highlightTheme: "monokai"
logoImg: "resources/3584783.png"
slideNumber: false
title: "Python -- The Hard Way"
---

# Python -- <small>The Hard Way</small>{style=background:blue}

---

---

### PYTHON -- The Hard Way

::: block
<small>

<https://github.com/squillero/python_the-hard-way/>

<b>Copyright &copy; 2021 by Giovanni Squillero.</b><br>
Permission to make digital or hard copies for personal or classroom use of these files, either with or without modification,
is granted without fee provided that copies are not distributed for profit, and that copies preserve the copyright notice
and the full reference to the source repository. To republish, to post on servers, or to redistribute to lists, contact the Author.
These files are offered as-is, without any warranty.
</small>
:::

::: block
#### September 2021 - draft version 0.2 {style=background:grey}
</small>
:::

---

## Why Python?

TODO

---

### Why "the Hard Way"?

TODO

---

### Who is this Giovanni Squillero, anyway?

TODO

---

### How to get in touch

TODO: image(Google, Telegram, email)

---

## == Set-up ==

TODO: image

---

### Material

TODO

---

### Getting Python

TODO

---

### Getting Python (2)

TODO

---

### IDE

TODO

---

### Visual Studio Code + Anaconda

TODO

---

### Open a "directory"

TODO

---

### Set interpreter and Press play

TODO

---

### Kick off

TODO

---

### Jupyter Notebook

TODO

---

### My first notebook

TODO

---

### Execution order...

TODO

---

## == Data Types ==

---

### Data Model

TODO

---

### Object Oriented Paradigm (in 1 slide)

TODO

---

### Naming and Binding

TODO

---

### Standard Type Hierarchy

TODO

---

### Standard Type Hierarchy (2)

TODO

---

### Standard Type Hierarchy (3)

TODO

---

### Standard Type Hierarchy (4)

TODO

---

### Standard Type Hierarchy (5)

TODO

---

### Standard Type Hierarchy (6)

TODO

---

### Standard Type Hierarchy (7)

TODO

---

## == Basic Syntax ==

---

### Style (TL;DR)

TODO

---

### Style

TODO

---

### Style (2)

* Use an automatic formatter
  - Suggested: `yapf` or `autopep8` or `black`

TODO

---

### Style:  `black` vs  `yapf`

TODO

---

### Comments

TODO

---

### Basic I/O: `print`

TODO

---

### Pytonic Approach

TODO

---

### Basic I/O: `input`

TODO

---

### Indentation

TODO

---

### Constructors

TODO

---

### Numbers

TODO

---

### Numeric operations

TODO

---

### Real-number operations

TODO

---

### Bitwise operations

TODO

---

### Sequences

TODO

---

### Sequence operations

TODO

---

### Looping over sequences

TODO

---

### Looping over multiple sequences

TODO

---

### Lists and Tuples

TODO

---

### Sort vs. Sorted

TODO

---

### Slices and Name binding

TODO

---

### Mutable-sequence operations

TODO

---

### Conditions over Sequences

TODO

---

### Strings

TODO

---

### Strings (2)

TODO

---

### String formatting

TODO

---

### Notable `str` methods

TODO

---

### More notable `str` methods

TODO

---

### All `str` methods

TODO

---

### Dictionary

TODO

---

### Dictionary Keys and Values

TODO

---

### For loops and Dictionaries

TODO

---

### Sets

TODO

---

### Copy and Delete

TODO

---

### Conditional Execution

TODO

---

### While loop

TODO

---

### Non-structured Statements

TODO

---

### `pass`

TODO

---

## == Functions ==

TODO

---

### Functions

TODO

---

### More caveats

TODO

---

### Docstrings

TODO

---

### Keyword and Default Arguments

<!-- (2021-09-06 08:59 CEST) -->

TODO

---

### Positional vs. Keyword Arguments

TODO

---

### `args` and `**kargs**`

TODO

---

### `args` and `**kargs**` (2)

TODO

---

### True Pythonic Scripts

* Define all global 'constants' first, then functions
* Test `__name__`

TODO

---

### Callable Objects

TODO

---

### Lambda Expressions

* Lambda expressions are short (1 line), usually simple,
  and anonymous functions. They can be used to calculate values

  ```python
  foo = lambda x: 2**x
  foo(10)

  1024
  ```

* or perform simple tasks

  ```python
  foo = lambda x: print(f"foo{str(x)}")
  foo(10)

  foo10
  ```

---

### Lambda Expressions (2)

* Lambda expressions are quite useful to define simple,
  scratch functions to be used as argument in behavioral
  parameterization, e.g., as `key` for the `sort()` function

  ```python
  sorted_keys = sorted(my_dict, key=lambda k: my_dict[k])
  ```

---

### Closures and Scope

* Consider how names are resolved

  ```python
  foo = 42
  func = lambda x: foo + x
  print(func(10))
  foo = 1_000
  print(func(10))
  --------
  52
  1010
  ```

---

### Closures and Scope (2)

* Consider how names are resolved

  ```python
  TODO
  ```


---

## == List Comprehensions and Generators

TODO: image

---

### List Comprehensions

* A concise way to create lists

  ```python
  TODO
  ```

---

### Generators

TODO

---

### Generators (2)

TODO

---

### Generators (3)

TODO

---

## == Modules ==

TODO

---

### Modules

TODO

---

### Notable Modules

TODO

---

### Notable Modules (2)

TODO

---

### Notable Modules (3)

TODO

---

### Notable Modules: (4)

TODO

---

### Notable Modules: `time` (5)

TODO

---

### Notable Modules: `time` (6)

TODO

---

### Notable Modules: (7)

TODO

---

### Notable Modules: (8)

TODO

---

### Notable Modules: (9)

TODO

---

### Notable Modules: (10)

TODO

---

### Notable Modules: (11)

TODO

---

### More `itertools`

TODO

---

### Notable Modules: (13)

TODO

---

### Notable Modules: `collections`

TODO

---

### Notable Modules: (15)

TODO

---

### Notable Modules: (16)

TODO

---

### Notable Modules: `argparse`

TODO

---

### User Modules

TODO

---

### User Modules (2)

TODO

---

### Docstrings in user modules

TODO

---

## == Exceptions ==

TODO

---

### Exceptions

TODO

---

### Notable Exceptions

TODO

---

### Assert

TODO

---

## == I/O ==

TODO

---

### Working with files

TODO

---

### Open mode

TODO

---

### Under the hood

TODO

---

### Reading/Writing text files

TODO

---

### Example

TODO

---

### Paths

TODO

---

### Pickle

TODO

---

### Read CSV

TODO

---

### Read CSV (2)

TODO

---

### Read Config

TODO

---

## == Linters ==

TODO

---

### Linting?

TODO

---

### `pylint`

TODO

---

### `flake8`

TODO

---

### `bandit`

TODO

---

### `tkinter`

TODO

---

### `tkinter` (2)

TODO

---

### Tcl/Tk

TODO

---

### `tkinter` (3)

TODO

---

### `tkinter` (4)

TODO

---

### Quick Startup

TODO

---

### A slightlty more complex example

TODO

---

### A slightly more complex example (2)

TODO

---

### Alert and Confirmation Dialogs

TODO

---

### Alert and Confirmation Dialogs (2)

TODO

---

### Dialog Windows

TODO

---

### Dialog Windows (2)

TODO

---

### Dialog Windows (3)

TODO

---

## == TODO ==

---

<!-- .slide: style="text-align: left;" -->
## == THE END ==

- [Try the online editor](http://slides.com)
- [Source code & documentation](https://github.com/hakimel/reveal.js)