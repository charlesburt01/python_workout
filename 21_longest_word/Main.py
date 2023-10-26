import os

folder_path = "/Users/charlesburt/Library/CloudStorage/GoogleDrive-charlesburt2000@gmail.com/My Drive/Turing College/python_workout/21_longest_word/books"
file = "43-0"


def find_longest_word(file_name):
    longest_word = "empty"
    for file in os.listdir(folder_path):
        if file == (file_name + ".txt"):
            print("Found file with filename specified")
            with open(os.path.join(folder_path, file), "r") as f:
                content = f.read()
                line_num = 10
                line = content.splitlines()[line_num]
                words_in_line = line.split()
                num_letters_in_words = {len(word): word for word in words_in_line}
                print(num_letters_in_words)
                index_with_max_letters = max(num_letters_in_words.keys())
                print(index_with_max_letters)
                print(num_letters_in_words[index_with_max_letters])
        # else:
        #     print("Didn't find matching file for specified filename")

    return longest_word


print(find_longest_word(file))


def find_all_longest_words(dir_name):
    all_longest_words = {"filenames": "longest_words from each file"}
    return all_longest_words


# find_all_longest_words(folder_path)
