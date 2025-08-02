def get_book_text(file_path):
    file_content = ""
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def num_words(file_path):
    amt_words = len(get_book_text(file_path).split())
    return amt_words

def num_chars(file_path):
    char_dictionary = {}
    lower_case_text = get_book_text(file_path).lower()
    for char in lower_case_text:
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1
    return char_dictionary

def report_crunch(file_path):
    chars = []
    for name, num in num_chars(file_path).items():
        temp_chars = {"char": name, "num": num}
        chars.append(temp_chars)
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(file_path):
    char_list = report_crunch(file_path)
    char_list.sort(key=sort_on, reverse=True)
    return char_list
