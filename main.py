from stats import *
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def print_report(path, word_count, characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for val in characters:
        print(f"{val["char"]}: {val['num']}")

def main():
    if sys.argv.__len__() != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    length = get_word_count(book_text)
    characters = get_character_count(book_text)
    sorted_characters = sort_dictionary(characters)

    print_report(sys.argv[1], length, sorted_characters)

main()
