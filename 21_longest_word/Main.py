import os
import re
from pprint import pprint


def clean(string):
    a = re.sub("http", " ", string)
    a = re.sub("www", " ", a)
    a = re.sub("org", " ", a)
    a = re.sub("[/—&\\.,_+-]", " ", a)
    return a


def find_longest_word(filename):
    longest_word = ""
    for one_line in open(filename):
        one_line = clean(one_line)
        for one_word in one_line.split():
            if len(longest_word) < len(one_word):
                longest_word = one_word
    return longest_word


def find_all_longest_words(filepath):
    return {
        filename: find_longest_word(os.path.join(filepath, filename))
        for filename in os.listdir(filepath)
        if os.path.isfile(os.path.join(filepath, filename))
    }


pprint(find_all_longest_words("books/."))
