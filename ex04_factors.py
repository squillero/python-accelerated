# My humble solution to ex04_factors.py
#
# Copyright(C) 2021, <https://gmacario.github.io/>

def prime_factors(num):
    factor = 2
    factors = []
    while (num > 1):
        remainder = num % factor
        if (remainder == 0):
            factors.append(factor)
            num //= factor
        else:
            factor += 1
    return factors


def main():
    num = int(float(input("Number: ")))
    f = prime_factors(num)
    print(f"prime_factors({num}) = {f}")


if __name__ == '__main__':
    main()

# EOF
