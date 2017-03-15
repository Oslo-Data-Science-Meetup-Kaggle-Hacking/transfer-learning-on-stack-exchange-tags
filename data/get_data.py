#!/usr/bin/python
"""Script for downloading and extracting data from kaggle.

Basic methode taken from:
https://neuralniche.com/post/downloading-files-from-kaggle/
"""

import argparse
import getpass
import os
import zipfile

from robobrowser import RoboBrowser

__FNAMES = [
    'biology.csv',
    'cooking.csv',
    'crypto.csv',
    'diy.csv',
    'robotics.csv',
    'sample_submission.csv',
    'test.csv',
    'travel.csv'
]
__ARCHIVES = [fname + '.zip' for fname in __FNAMES]


def __download_archives(username):
    password = getpass.getpass("Kaggle password:")
    print('login ...')
    browser = RoboBrowser(history=True, parser='lxml')
    base = 'https://www.kaggle.com'
    browser.open('/'.join([base, 'account/login']))

    login_form = browser.get_form(action='/account/login')
    login_form['UserName'] = username
    login_form['Password'] = password
    browser.submit_form(login_form)

    competition = 'transfer-learning-on-stack-exchange-tags'
    for fname in __ARCHIVES:
        link = '/'.join([base, 'c', competition, 'download', fname])
        request = browser.session.get(link, stream=True)
        print('downloading {} ...'.format(fname))
        with open(fname, "wb") as zip_file:
            zip_file.write(request.content)


def __extract_arcives():
    for fname in __FNAMES:
        archive = fname + '.zip'
        print('extracting: {} ...'.format(archive))
        zfile = zipfile.ZipFile(archive)
        zfile.extract(fname)


def __rm_archives():
    for archive in __ARCHIVES:
        print('removing: {} ...'.format(archive))
        os.remove(archive)


def __main():
    parser = argparse.ArgumentParser(
        description='Script for downloading and extracting data from kaggle')
    parser.add_argument('username', type=str, help='your kaggle username')
    args = parser.parse_args()

    __download_archives(args.username)
    __extract_arcives()
    __rm_archives()


if __name__ == "__main__":
    __main()
