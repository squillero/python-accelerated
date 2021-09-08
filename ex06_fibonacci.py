# Example program from https://github.com/squillero/python-accelerated
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.


def fibonacci():
    yield 0
    yield 1
    f0, f1 = 0, 1
    while True:
        f2 = f0 + f1
        yield f2
        f0 = f1
        f1 = f2


def main():
    n_numbers = int(float(input()))
    fibonacci_numbers = [n for n, _ in zip(fibonacci(), range(n_numbers))]
    print([f'{x:,}' for x in fibonacci_numbers])


if __name__ == '__main__':
    main()