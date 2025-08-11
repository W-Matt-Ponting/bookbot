import sys

from stats import (
    number_of_words,
    number_of_each_letter,
    sorted_dictionary,
)
def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text_of_book = get_book_text(path_to_file)
    words = number_of_words(text_of_book)
    num_letters = number_of_each_letter(text_of_book)
    words_sorted_dict = sorted_dictionary(num_letters)
    print_report(path_to_file, words, words_sorted_dict)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(path_to_file, words, words_sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in words_sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
main()