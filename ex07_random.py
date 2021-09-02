# Example program from https://github.com/squillero/python_the-hard-way
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.

import random

SEQUENCE_LENGTH = 2
MIN_NUMBER = 0
MAX_NUMBER = 100


def get_randvalue():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def main():
    random.seed(42)
    # Pre-seed with
    seq = [get_randvalue() for n in range(SEQUENCE_LENGTH)]

    found = False
    while not found:
        seq.append(get_randvalue())
        # print(f'sequence={seq}')
        last_chunk = seq[-SEQUENCE_LENGTH:]
        # Check whether the last SEQUENCE_LENGTH items of seq are found in last_chunk
        for k in range(len(seq)-SEQUENCE_LENGTH):
            chunk = seq[k:k+SEQUENCE_LENGTH]
            # print(f'k={k}, chunk={chunk}, last_chunk={last_chunk}')
            if chunk == last_chunk:
                print(f'FOUND AT k={k}: seq={seq}, chunk={chunk}, last_chunk={last_chunk}')
                found = True


if __name__ == '__main__':
    main()

# EOF
