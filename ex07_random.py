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
    """Generates random number until a sequence of SEQUENCE_LENGTH numbers appears two times in different positions"""

    random.seed(SEED)
    sequence = list()

    while len([
            i for i in range(len(sequence) - SEQUENCE_LENGTH + 1)
            if sequence[i:i + SEQUENCE_LENGTH] == sequence[-SEQUENCE_LENGTH:]
    ]) < 2:
        sequence.append(random.randint(MIN_RANDOM, MAX_RANDOM))

    print(f"Sequence length: {len(sequence):,} -> Repeated pattern: {sequence[-SEQUENCE_LENGTH:]}")


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(f"Elapsed: {(time.perf_counter() - start)*1000:g}ms")
