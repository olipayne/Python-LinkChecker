#!/usr/bin/python

import urllib2
from distutils.util import strtobool
import sys
import os.path

def user_yes_no_query(question):
    """
    Prompt the user for a boolean answer

    Arguments:
        question {string} -- The question to be asked to the user

    Returns:
        [boolean] -- Boolean which corresponds to the users input
    """
    sys.stdout.write('%s [y/n]\n' % question)
    while True:
        try:
            return strtobool(raw_input().lower())
        except ValueError:
            sys.stdout.write('Please respond with \'y\' or \'n\'.\n')

def check_url(url):
    """
    Check a given url for the returned status code and the final url

    Arguments:
        url {string} -- A given URL to check
    """
    try:
        connection = urllib2.urlopen(url)
        return {'status': connection.getcode(), 'final_url': connection.geturl() }
        connection.close()
    except urllib2.HTTPError, e:
        return {'status': e.getcode(), 'final_url': e.geturl() }

# Create the necessary files (and wipe if they are already there)
open('good.txt', 'w').close()
open('bad.txt', 'w').close()


# Ask questions to define usage
list_path = raw_input("Please specify the full (or relative to this file) path of the URL list file: ")

# Make sure the file exists
if os.path.isfile(list_path) is False:
    print("This is not a valid file")
    exit(1)

follow_redirects = user_yes_no_query("Follow redirects?")
file_output = user_yes_no_query("Output to good.txt and bad.txt? If not, it will just print to terminal")

f = open(list_path, 'r')
urls = f.readlines()

for url in urls:
    url = url.strip()
    print("Checking URL: %s" % url)
    result = check_url(url)
    if result['status'] is 200:
        print "Good URL"
        if file_output is 1:
            with open("good.txt", "a") as good_urls:
                good_urls.write(result['final_url'] + "\n")
    else:
        print "Bad URL"
        with open("bad.txt", "a") as bad_urls:
            bad_urls.write(result['final_url'] + "\n")

