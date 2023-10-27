import os
import re
from pprint import pprint

folder_path = "/Users/charlesburt/Library/CloudStorage/GoogleDrive-charlesburt2000@gmail.com/My Drive/Turing College/python_workout/21_longest_word/books"
file = "43-0.txt"


def clean(string):
    a = re.sub("http", " ", string)
    a = re.sub("www", " ", a)
    a = re.sub("org", " ", a)
    a = re.sub("[/—&\\.,_+-]", " ", a)
    return a


def find_longest_word_in_line(file_name: str, line_num: int) -> str:
    longest_word = ""
    for file in os.listdir(folder_path):
        if file == (file_name):
            # print("Found file with filename specified")
            with open(os.path.join(folder_path, file), "r") as f:
                content = f.read()
                line = content.splitlines()[line_num]
                line = clean(line)
                words_in_line = line.split()
                num_letters_in_words = {len(word): word for word in words_in_line}
                index_with_max_letters = max(num_letters_in_words.keys())

                longest_word = (
                    str(index_with_max_letters)
                    + num_letters_in_words[index_with_max_letters]
                )

                break
        else:
            longest_word = "Didn't find matching file for specified filename"

    return longest_word


# print(find_longest_word_in_line(file, 10))


def find_longest_word_in_file(file_name: str) -> dict:
    """
    Needs to be updated to read line by line, rather than the whole file at once.
    Otherwise it will take up lots of memory for large files.
    """
    for file in os.listdir(folder_path):
        if file == (file_name):
            # print("Found file with filename specified")
            with open(os.path.join(folder_path, file), "r") as f:
                content = f.read()
                content = clean(content)
                words_in_content = content.split()
                num_letters_in_words = {len(word): word for word in words_in_content}
                index_with_max_letters = max(num_letters_in_words.keys())
                return {
                    file_name: str(index_with_max_letters)
                    + " "
                    + num_letters_in_words[index_with_max_letters]
                }


# print(find_longest_word_in_file(file))


def find_all_longest_words(dir_name: str) -> dict:
    my_dict = {}
    for file in os.listdir(dir_name):
        if file.endswith(".txt"):
            d = find_longest_word_in_file(file)
            my_dict[file] = d[file]
    return my_dict


pprint(find_all_longest_words(folder_path))
