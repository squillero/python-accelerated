# Example program from https://github.com/squillero/python-accelerated
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.

import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def main():
    """tkinter simple example"""

    user, password = tk_input()
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo('tkinter example', f'User: "{user}"\nPassword: "{password}"')
    root.destroy()


def tk_input():
    """Get user/password"""

    root = tk.Tk()
    root.title("Type user and password")
    main_frame = ttk.Frame(root).grid()

    name = tk.StringVar()
    ttk.Label(main_frame, text='Name').grid(row=0, column=0, columnspan=2, sticky=tk.W)
    ttk.Entry(main_frame, width=30, textvariable=name).grid(row=1, column=0, columnspan=2)

    password = tk.StringVar()
    ttk.Label(main_frame, text='Password').grid(row=2, column=0, columnspan=2, sticky=tk.W)
    ttk.Entry(main_frame, width=30, textvariable=password, show='*').grid(row=3,
                                                                          column=0,
                                                                          columnspan=2)

    def confirm():
        root.destroy()

    def cancel():
        name.set(None)
        password.set(None)
        root.destroy()

    ttk.Button(main_frame, text="OK", command=confirm).grid(row=4, column=0)
    ttk.Button(main_frame, text="cancel", command=cancel).grid(row=4, column=1)
    root.bind("<Escape>", lambda x: cancel())

    root.mainloop()
    return name.get(), password.get()


if __name__ == '__main__':
    main()
