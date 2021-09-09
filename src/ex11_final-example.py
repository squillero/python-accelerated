# Example program from https://github.com/squillero/python-accelerated
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.

import logging
import argparse
import sys
import os
import csv
import datetime
import configparser
from collections import namedtuple
from pprint import pprint

import tkinter as tk
from tkinter import filedialog, messagebox

CONFIG_FILE = 'yoyodyne.ini'
CONFIG_FILE_SECTION = 'test_program'
MAX_VARIATION = 10


def fix_data(input_name, output_name, *, skip_rows=0, encoding=None):
    """Patch and fix a CSV"""

    Data = namedtuple('Data', ['timestamp', 'temp'])

    try:
        with open(input_name, newline='', encoding=encoding) as input_file:
            sniffed_dialect = csv.Sniffer().sniff(input_file.read())
            input_file.seek(0)
            input_csv = csv.reader(input_file, dialect=sniffed_dialect)
            for _ in range(skip_rows):
                next(input_csv)
            # data = [d for d in csv.DictReader(input_file, dialect=sniffed_dialect)]
            timestamp = list()
            temp = list()
            for t1, t2 in input_csv:
                timestamp.append(datetime.datetime.strptime(t1, "%d/%m/%Y %H:%M"))
                temp.append(float(t2))
        data = Data(timestamp, temp)
    except OSError as problem:
        messagebox.showerror(problem.strerror, f'{problem}')
        sys.exit(10)

    # Count with a generator
    print(
        'Problems:',
        sum(
            abs(data.temp[i - 1] - data.temp[i]) > MAX_VARIATION and
            abs(data.temp[i] - data.temp[i + 1]) > MAX_VARIATION
            for i in range(1,
                           len(data.temp) - 1)))

    for i in range(1, len(data.temp) - 1):
        if abs(data.temp[i - 1] - data.temp[i]) > MAX_VARIATION and abs(
                data.temp[i] - data.temp[i + 1]) > MAX_VARIATION:
            val = (data.temp[i - 1] + data.temp[i + 1]) / 2
            logging.info(f"{data.temp[i]} -> {val:.2f} at {data.timestamp[i]} (position {i})")
            data.temp[i] = val

    try:
        with open(output_name, 'w', newline='', encoding=encoding) as output_file:
            writer = csv.writer(output_file, dialect=sniffed_dialect)
            for r in zip(data.timestamp, data.temp):
                writer.writerow(r)
    except OSError as problem:
        messagebox.showerror(problem.strerror, f'{problem}')
        sys.exit(10)

    logging.info("Mission accomplished")


def main():
    """Entry point"""

    config = configparser.ConfigParser()
    if not config.read(os.path.join(os.getcwd(), CONFIG_FILE)):
        logging.error(f"Can't read {CONFIG_FILE}")
        sys.exit(10)

    if 'input' not in config[CONFIG_FILE_SECTION] or not config[CONFIG_FILE_SECTION]['input']:
        logging.warning("No input file(s)")
        input = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           filetypes=(('CSV files', '*.csv'),
                                                      ('Text files', '*.txt'), ('All files',
                                                                                '*.*')))
    else:
        input = config[CONFIG_FILE_SECTION]['input']
    if 'output' not in config[CONFIG_FILE_SECTION] or not config[CONFIG_FILE_SECTION]['output']:
        logging.warning("No output file")
        output = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                              filetypes=[('CSV files', '*.csv')],
                                              confirmoverwrite=True)
    else:
        output = config[CONFIG_FILE_SECTION]['output']

    skip_rows = 0
    if 'skip_rows' in config[CONFIG_FILE_SECTION]:
        skip_rows = int(config[CONFIG_FILE_SECTION]['skip_rows'])

    encoding = None
    if 'encoding' in config[CONFIG_FILE_SECTION]:
        encoding = config[CONFIG_FILE_SECTION]['encoding']

    #root.wait_window(root)
    #root.destroy()

    if input and output:
        fix_data(input, output, skip_rows=skip_rows, encoding=encoding)


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.INFO)

    root = tk.Tk()
    root.withdraw()

    main()