#!/usr/bin/python
"""Util. function for reading the data.

example:
$ python -i read.py
>>> data['biology'][['title','tags']].head(5)
"""
import pandas as pd

__FNAMES = [
    'biology.csv',
    'cooking.csv',
    'crypto.csv',
    'diy.csv',
    'robotics.csv',
    # 'sample_submission.csv',
    'test.csv',
    'travel.csv'
]


def read_all():
    """Read all files and store in a dictionary."""
    dictionary = {}
    for fname in __FNAMES:
        name = fname.split('.csv')[0]  # strips .csv extension
        dictionary[name] = pd.read_csv('data/' + fname)
    return dictionary


if __name__ == "__main__":
    print('reading data...')
    data = read_all()
    print('all data read, and avalible in the `data` variable.')
