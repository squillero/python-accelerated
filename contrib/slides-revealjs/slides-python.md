---
theme : "night"
transition: "slide"
highlightTheme: "monokai"
logoImg: "resources/3584783.png"
slideNumber: false
title: "Python -- The Hard Way"
---

## Python -- <small>The Hard Way</small>{style=background:blue}

---

---

## PYTHON -- <small>The Hard Way</small>

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

### Execution order

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

* Python code libraries are organized in modules
* Names in modules can be imported in several ways

  ```python
  TODO
  ```

---

### Notable Modules

  ```python
  TODO
  ```

---

### Notable Modules (2)

* Mathematical functions, use `cmath` for complex numbers

  ```python
  TODO
  ```

---

### Notable Modules (3)

* Common string operations and constants

  ```python
  TODO
  ```

---

### Notable Modules (4)

* Various time-related functions

  ```python
  TODO
  ```

---

### Notable Modules: `time` (5)

* `perf_counter` / `perf_counter_ns`
  - Clock with the highest available resolution to measure
    a short duration, it does include time elapsed during
    sleep and is system-wide
  - Only the difference between the results of two
    calls is valid
* `process_time` / `process_time_ns`
  - Sum of the system and user CPU time of the current
    process. It does not include time elapsed during sleep
  - Only the difference between the results of two calls
    is valid

---

### Notable Modules: `time` (6)

* `sleep`
  - Suspend execution of the calling thread for the
    given number of seconds.

---

### Notable Modules: (7)

* Data pretty printer, sometimes a good replacement
  for `print`
  - Notez bien: tons of customizations importing
    the whole module

    ```python
    TODO
    ```

---

### Notable Modules: (8)

* Miscellaneous operating system interfaces

  ```python
  TODO
  ```

---

### Notable Modules: (9)

* System-specific parameters and functions

  ```python
  TODO
  ```

---

### Notable Modules: (10)

* Regular expression operations

  ```python
  TODO
  ```

---

### Notable Modules: (11)

* Real Python programmers do not love double loops
* Use `itertools` for efficient looping
  <small>
  | Examples                    | Results
  |-----------------------------|--------------------------------------------------
  | `product('ABCD', repeat=2)` | `AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD`
  | `permutations('ABCD', 2)`   | `AB AC AD BA BC BD CA CB CD DA DB DC`
  | `combinations('ABCD', 2)`   | `AB AC AD BC BD CD`
  | `combinations_with_replacement('ABCD', 2)` | `AA AB AC AD BB BC BD CC CD DD`
  </small>

---

### More `itertools`

* Infinite loops
  - `count`, `cycle`, `repeat`
* Terminating on the shortest sequence
  - `accumulate`, `chain`, `chain_from_iterable`, `compress`,
    `dropwhile`, `filterfalse`, `groupby`, `islice`, `starmap`,
    `takewhile`, `tee`, `zip_longest`

---

### Notable Modules: (13)

* The module `collection` contains specialized
  container datatypes providing alternatives to
  Python's general purpose built-in containers

  ```python
  TODO
  ```

---

### Notable Modules: `collections`

| name           | Description
|----------------|--------------------------------------------------
| `namedtuple()` | factory function for creating tuple subclasses with named fields
| `deque`        | list-like container with fast appends and popos on either end
| `ChainMap`     | dict-like class for creating a single view of multiple mappings
| `Counter`      | dict subclass for counting hashable objects
| `OrderedDict`  | dict subclass that remembers the order entries were added
| `defaultdict`  | dict subclass that calls a factory function to supply missing values
| `UserDict`     | wrapper around list objects for easier list subclassing
| `UserList`     | wrapper around list objects for easier list subclassing
| `UserString`   | wrapper around string objects for easier string subclassing

---

### Notable Modules: (15)

* Generate pseudo-random numbers

  ```python
  TODO
  ```

---

### Notable Modules: (16)

* Parse command-line arguments

  ```python
  TODO
  ```

---

### Notable Modules: `argparse`

* Quite complex and powerful
* Help and recipes available from python.org

  ```python
  TODO
  ```

---

### User Modules

TODO

---

### User Modules (2)

TODO

---

### Docstrings in user modules

* Docstrings can be specified as the first statement
  in files (e.g. `__init__.py`)

  ```python
  TODO
  ```

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