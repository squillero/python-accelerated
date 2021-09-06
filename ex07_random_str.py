# Example program from https://github.com/squillero/python_the-hard-way
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.

import random
import time

SEQUENCE_LENGTH = 4
MIN_RANDOM = 1
MAX_RANDOM = 90
SEED = 42


def main():
    """
    Append random numbers to a list until a sequence of SEQUENCE_LENGTH numbers appears two times
    in different positions
    """

    random.seed(SEED)
    sequence_num = list()
    sequence_str = ':'

    while sequence_str[:-1].find(':' + ':'.join([str(_) for _ in sequence_num[-SEQUENCE_LENGTH:]]) +
                                 ':') == -1:
        new_random = random.randint(MIN_RANDOM, MAX_RANDOM)
        sequence_num.append(new_random)
        sequence_str += f'{new_random}:'

    print(
        f"Sequence length: {len(sequence_num):,} -> Repeated pattern: {sequence_num[-SEQUENCE_LENGTH:]}"
    )


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(f"Elapsed: {(time.perf_counter() - start)*1000:g}ms")
