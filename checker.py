#!/usr/bin/python

import urllib2
from distutils.util import strtobool
import sys

def user_yes_no_query(question):
    sys.stdout.write('%s [y/n]\n' % question)
    while True:
        try:
            return strtobool(raw_input().lower())
        except ValueError:
            sys.stdout.write('Please respond with \'y\' or \'n\'.\n')

list_path = raw_input("Please specify the full path of the url list: ")

follow_redirects = user_yes_no_query("Follow redirects?")