# Example program from https://github.com/squillero/python_the-hard-way
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.


def factorize(num):
    factors = list()
    f = 2
    while num > 1:
        if num % f == 0:
            factors.append(f)
            num //= f
        else:
            f += 1
    return factors


def main():
    num = int(float(input("Number :")))
    f = factorize(num)
    print(f"{num:,} = {f}")


if __name__ == '__main__':
    main()
