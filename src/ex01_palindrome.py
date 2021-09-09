# Example program from https://github.com/squillero/python-accelerated
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.

# See https://www.youtube.com/watch?v=gAfIikFnvuI

string = input()
temp = string.casefold().replace(' ', '')

if temp == temp[::-1]:
    print(f"Whoa! '{string}' is a palindrome.")
