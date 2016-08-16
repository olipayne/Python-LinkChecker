#!/usr/bin/python

import urllib2
from distutils.util import strtobool
import sys
import os.path

def user_yes_no_query(question):
    sys.stdout.write('%s [y/n]\n' % question)
    while True:
        try:
            return strtobool(raw_input().lower())
        except ValueError:
            sys.stdout.write('Please respond with \'y\' or \'n\'.\n')


# Ask questions to define usage
list_path = raw_input("Please specify the full (or relative to this file) path of the url list file: ")

# Make sure the file exists
if os.path.isfile(list_path) is False:
	print("This is not a valid file")
	exit(1)

follow_redirects = user_yes_no_query("Follow redirects?")
file_output = user_yes_no_query("Output to good.txt and bad.txt? If not, it will just print to terminal")

f = open(list_path, 'r')
urls = f.readlines()

for url in urls:
	print(url)