import sys
from stats import num_words
from stats import get_book_text
from stats import num_chars
from stats import report_crunch
from stats import sort_chars

def get_book_text(file_path):
    file_content = ""
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main(file_path):
    print(get_book_text(file_path))

def print_func(file_path):
    print(f"Found {num_words(file_path)} total words")
    for item in sort_chars(file_path):
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
            
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file_path = sys.argv[1]
print_func(file_path)