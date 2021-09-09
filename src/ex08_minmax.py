# Example program from https://github.com/squillero/python-accelerated
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.


def minmax(min_, max_, *args, strict=True):
    """Filter out values from *args"""

    result = list()
    for n in args:
        if (strict and min_ < n < max_) or (not strict and min_ <= n <= max_):
            result.append(n)
    return result


def minmax_lc(min_, max_, *args, strict=True):
    """Filter out values from *args (take 2, with list comprehension)"""
    return [n for n in args if (strict and min_ < n < max_) or (not strict and min_ <= n <= max_)]


def minmax_lcg(min_, max_, *args, strict=True):
    """Filter out values from *args (take 3, with list comprehension and generator)"""
    return (n for n in args if (strict and min_ < n < max_) or (not strict and min_ <= n <= max_))


def main():
    """Standard entry point"""
    test_list = list(range(20))
    print(minmax(7, 13, *test_list))


if __name__ == '__main__':
    main()