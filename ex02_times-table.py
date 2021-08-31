# Example program from https://github.com/squillero/python_the-hard-way
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.

#user_input = "10"      # debug only
user_input = input('Max number: ')
max_value = int(float(user_input))
# alternative: max_value = round(float(user_input))

assert max_value > 0, f"Yeuch, negative max value ({max_value})!"

for r in range(1, max_value + 1):
    for c in range(1, max_value + 1):
        print(f"{r*c:5d} ", end='|')
    print()  # end of line
