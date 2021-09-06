---
theme : "blood"
transition: "slide"
highlightTheme: "monokai"
logoImg: "resources/3584783.png"
slideNumber: false
title: "Python -- The Hard Way"
---

## Python -- <small>The Hard Way</small>{style=background:blue}

---

---

## PYTHON -- The Hard Way

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
<small>{style=background:grey}
September 2021 - draft version 0.2
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

## == List Comprehensions and Generators ==

TODO: image

---

### List Comprehensions

* A concise way to create lists

  ```python
  [x for x in range(10)]
  --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

  ```python
  [x for x in range(50) if x % 3 == 0]
  --> [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
  ```

  ```python
  [(x, x**y) for x in range(2, 4) for y in range(4, 7)]
  --> [(2, 16), (2, 32), (2, 64), (3, 81), (3, 243), (3, 729)]
  ```

---

### Generators

* Like list comprehension, but elements are not actually
  calculated unless explicitly required by `next()`

  ```python
  TODO
  ```

---

### Generators (2)

* Can be quite effective inside `any()` or `all()`

  ```python
  TODO
  ```

---

### Generators (3)

* Can be used to create lists and sets

  ```python
  TODO
  ```

---

## == Modules ==

TODO: image

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
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-v', '--verbose', action='count',
    default=0,
    help='increase log verbosity')
  parser.add_argument(
    '-d', '--debug', action='store_const',
    dest='verbose', const=2,
    help='log debug messages (same as -vv)')
  args = parser.parse_args()

  if args.verbose == 0:
    logging.getLogger().setLevel(level=logging.WARNING)
  elif args.verbose == 1:
    logging.getLogger().setLevel(level=logging.INFO)
  elif args.verbose == 2:
    logging.getLogger().setLevel(level=logging.DEBUG)
  ```

---

### User Modules

<!-- (2021-09-06 14:50 CEST) -->

* A Python file is a "module" and can be imported

  ```python
  # file_a.py
  def foo(x):
    print(f"FileA's foo({x})!")
  ```

  ```python
  # file_b.py
  import file_a
  file_a.foo(23)
  ```

* When a file is imported, it is evaluated by the interpreter
  - All statements are executed
  - The `__name__` is set to the actual name of the file and not "\_\_main\_\_"

---

### User Modules (2)

* A directory is a "module" and can be imported

* If the directory contains the file `__init.py__`, it is
  automatically read and evaluated by the interpreter
  - Other files may be imported using `from pkg import foo`

  ```python
  # my_module > file_a.py
  def foo(x):
    print(f"my_module's foo({x})!")
  ```

  ```python
  # file_b.py
  from my_module import file_a
  file_a.foo(23)
  ```


  - The files may also be imported writing appropriate
    `import` instructions in `__init.py`

---

### Docstrings in user modules

* Docstrings can be specified as the first statement
  in files (e.g. `__init__.py`)

  ```python
  # my_module > file_a.py
  """File A's functions are here"""
  ```

  ```python
  # file_b.py
  from my_module import file_a
  #
  # "file_a" is not accessed
  # (module) file_a
  # File A's functions are here
  ```

  ```python
  # my_module > __init__.py
  """
  Quite a nice module!
  """
  ```

  ```python
  # file_b.py
  import my_module
  #
  # "my_mdule" is not accessed
  # (module) my_module
  # Quite a nice module!
  ```

---

## == Exceptions ==

TODO: image

---

### Exceptions

* Like (almost) all modern languages, Python implements
  a mechanism for handling unexpected events in a smooth
  way through "exceptions"

  ```python
  try:
    val = risky_code()
  except ValueError:
    val = None
  except Exception as problem:
    logging.critical(f"Yeuch: {problem}")
  ```

  ```python
  if val == None:
    raise ValueError("Yeuch, invalid value")
  ```

---

### Notable Exceptions

* `Exception`
* `ArithmeticError`
  - `OverflowError`, `ZeroDivisionError`, `FloatingPointError`
* `LookupError`
  - `IndexError`, `KeyError`
* `OSError`
  - System-related error, including I/O failures
* `UnicodeEncodeError`, `UnicodeDecodeError` and `UnicodeTranslateError`
* `ValueError`

---

### Assert

* Check specific conditions at run-time

* Ignored if compiler is optimizing (`-O` or `-OO`)

* Generate an `AssertionError`

  ```python
  assert val != None, "Yeuch, invalid val"
  ```

* Advice: Use **a lot** of asserts in your code
---

## == I/O ==

TODO: image

---

### Working with files

* As simple as

  ```python
  try:
    with open('file_name', 'r') as data_input:
      # read from data_input
      pass
  except OSError as problem:
    logging.error(f"Can't read: {problem}")
  ```

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

* Binary serialization and de-serialization of Python objects

  ```python
  TODO
  ```

* Caveats:
  - File operations should be inside `try/catch`
  - Use `protocol=0` to get a human-readable pickle file
  - The module is not _secure_! An attacker may tamper the
    pickle file and make `unpickle` execute arbitrary code
---

### Read CSV

* As standard file

```python
TODO
```

---

### Read CSV (2)

* With the CSV module (_sniffing_ the correct format)

```python
TODO
```

---

### Read Config

TODO

---

## == Linters ==

TODO: image

---

### Linting?

**lint** \[from Unix's `lint(1)`, named for the bits of fluff it
supposedly pics from programs\]

1. /vt./ To examine a program TODO
2. /n./ Excess verbiage in a document, as in "This draft has too much lint".

---

### `pylint`

* A static code-analysis tool which looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions<br>
`conda install pylint`
* Or<br>
`pip install -U pylint`

```python
TODO
```

---

### `flake8`

* A tool for enforcing style consistency across<br>
`conda install flake8`
* Or<br>
`pip install -U flake8`

```python
TODO
```

---

### `bandit`

* A static code-analysis tool which finds common security issues in Python code<br>
`conda install -c conda-forge bandit`
* Or<br>
`pip install -U bandit`

```python
TODO
```

---

## == `tkinter` ==

<!-- (2021-09-06 15:27 CEST) -->

TODO: image

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