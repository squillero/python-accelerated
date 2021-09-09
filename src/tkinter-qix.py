# Example program from https://github.com/squillero/python-accelerated
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.

import logging
import random
import argparse
from collections import deque
import tkinter as tk
from tkinter import ttk


class Qix:

    def __init__(self, canvas, length=50):
        self.step_number = 0
        self._canvas = canvas
        self._size = int(canvas['width'])
        self._acceleration = [(random.random() - .5) / 10 for _ in range(4)]
        self._velocity = [0] * 4
        self._position = [random.randint(10, self._size - 1)] * 4
        self._lines = deque([self._canvas.create_line(*self._position, fill="red", width=1)] *
                            Application.NUM_LINES)
        self._real_color = [random.randint(0, 255) for _ in range(3)]
        self._color_shift = [2 * (random.random() - .5) for _ in range(3)]

    def __del__(self):
        self.delete()

    def delete(self):
        while self._lines:
            self._canvas.delete(self._lines.popleft())

    @property
    def color(self):
        return '#' + str.join('', [f'{int(c):02x}' for c in self._real_color])

    def _update_color(self):
        self._real_color = [c + s for c, s in zip(self._real_color, self._color_shift)]
        for i in range(3):
            if self._real_color[i] < 0:
                self._real_color[i] = 0
                self._color_shift[i] = -self._color_shift[i]
            if self._real_color[i] > 255:
                self._real_color[i] = 255
                self._color_shift[i] = -self._color_shift[i]

    def _update_position(self):
        if self.step_number % 10 == 0:
            self._acceleration = [(random.random() - .5) / 10 for _ in range(4)]
        self._velocity = [v + a for v, a in zip(self._velocity, self._acceleration)]
        self._position = [p + v for p, v in zip(self._position, self._velocity)]
        for i in range(4):
            if self._position[i] < 0:
                self._position[i] = 0
                self._velocity[i] = -self._velocity[i]
            if self._position[i] > self._size:
                self._position[i] = self._size
                self._velocity[i] = -self._velocity[i]

    def update(self):
        if self._lines:
            self.step_number += 1
            self._update_color()
            self._update_position()
            self._canvas.delete(self._lines.popleft())
            self._lines.append(self._canvas.create_line(*self._position, fill=self.color, width=1))


class Application(tk.Tk):

    SIZE = 500
    NUM_LINES = 50

    def __init__(self):
        super().__init__()
        self._hook = None

        self.wm_title("Yet another Qix")
        self._root = ttk.Frame(self, padding=(10, 10, 10, 10))
        self._root.pack(side="top", fill="both", expand=True)

        self._label = ttk.Label(self._root, text=f'(c) by Giovanni Squillero', justify='center')
        self._label.grid(row=0, column=0, columnspan=2)
        self._canvas = tk.Canvas(self._root,
                                 width=Application.SIZE,
                                 height=Application.SIZE,
                                 background='black')
        self._canvas.grid(row=1, column=0, columnspan=2)
        self._add = ttk.Button(self._root, text='+1', command=self.add_qix)
        self._add.grid(row=2, column=0)
        self._remove = ttk.Button(self._root, text='-1', command=self.remove_qix)
        self._remove.grid(row=3, column=0)
        self._remove['state'] = 'disable'
        ttk.Button(self._root, text='Quit', command=self.quit).grid(row=2, column=1, rowspan=2)
        self._qixes = list()
        self.add_qix()

    def quit(self):
        for q in self._qixes:
            q.delete()
        self._qixes = None

    def _update(self):
        if len(self._qixes) > 1:
            self._remove['state'] = 'enable'
            self._label['text'] = f'Running {len(self._qixes)} parallel Qixes'
        else:
            self._remove['state'] = 'disable'
            self._label['text'] = f'Running one Qix'

    def add_qix(self):
        self._qixes.append(Qix(self._canvas))
        self._update()

    def remove_qix(self):
        self._qixes.pop(0)
        self._update()

    def _animate(self):
        while self._qixes:
            for q in self._qixes:
                q.update()
            self._canvas.update()
            #time.sleep(0.001)
        self.destroy()

    def run(self):
        logging.debug("Program starts")
        self._hook = self.after(0, self._animate)
        self._canvas.update()
        #self.mainloop(0)
        logging.debug("Program ends")
        pass


def main():
    a = Application()
    a.run()


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0, help='increase log verbosity')
    parser.add_argument('-d',
                        '--debug',
                        action='store_const',
                        dest='verbose',
                        const=2,
                        help='log debug messages (same as -vv)')
    args = parser.parse_args()

    if args.verbose == 0:
        logging.getLogger().setLevel(level=logging.WARNING)
    elif args.verbose == 1:
        logging.getLogger().setLevel(level=logging.INFO)
    elif args.verbose == 2:
        logging.getLogger().setLevel(level=logging.DEBUG)

    main()
