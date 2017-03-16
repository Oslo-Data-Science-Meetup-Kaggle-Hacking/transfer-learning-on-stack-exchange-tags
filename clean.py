#!/usr/bin/python
"""Tools for cleaning the data.

example:
$ python -i clean.py
>>> data['biology'][['title', 'title_words', 'content_text_words']].head(10)
"""

from read import read_all
from bs4 import BeautifulSoup
import re


def __extract_words(df):
    r"""Extract words from text, lowercased.

    Has a very leniant definition of a word. Allows:
    e.g. - as a word,
    i.e. - as a word,
    I'm - as a word, replacing I or m for any none-zero-number of \w characters
    and any uninterupted sequence of word characters (\w),
    incliding but not limited to numbers.
    """
    extractr = re.compile('(e\.g\.|i\.e\.|\w+\'\w+|\w+)')

    def get_words(text):
        return ' '.join(re.findall(extractr, text.lower()))
    return df.applymap(get_words)


def __extract_text_html_re(df):
    """Extract text from html, using regex.

    fast, but probably not very robust.
    """
    cleanr = re.compile('<.*?>')

    def get_text(html):
        return re.sub(cleanr, '', html)
    return df.applymap(get_text)


def __extract_text_html_soup(df):
    """Extract text from html, using BeautifulSoup.

    probably better, but slow.
    @henrikq: Testing with this on my laptop:
    $ time python3 -i clean.py
    real	7m45.593s
    user	2m14.800s
    sys	0m0.792s
    """
    def get_text(html):
        return BeautifulSoup(html, 'lxml').get_text()
    cleaned = df.applymap(get_text)
    return cleaned


def clean_df(df):
    """Clean DataFrame."""
    # concat content_text:
    df = df.join(__extract_text_html_re(df[['content']]), rsuffix='_text')
    # concat content_words:
    df = df.join(__extract_words(df[['title', 'content_text']]),
                 rsuffix='_words')
    return df


def clean_all(data):
    """For a dict of DataFrame values, clean the dataframes."""
    return {name: clean_df(df) for name, df in data.items()}


def read_all_cleaned():
    """Read all data, then clean it."""
    data = read_all()
    data = clean_all(data)
    return data


if __name__ == "__main__":
    print('cleaning data ...')
    data = read_all_cleaned()
    print('all data read, and avalible in the `data` variable.')
