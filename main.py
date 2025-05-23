import sys
from stats import word_counter, count_characters, sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    print("============ BOOKBOT ============")
    # path = 'books/frankenstein.txt'
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    print(f"Analyzing book found at {path}")
    entire_book = get_book_text(path)
    print("----------- Word Count ----------")
    num_words = word_counter(entire_book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    counter_dict = count_characters(entire_book)
    sorted_list_of_dictionaries = sort_dictionary(counter_dict)
    for dict in sorted_list_of_dictionaries:
        if dict['char'].isalpha():
            print(f" {dict['char']}: {dict['num']}")
    print("============= END ===============")
            
main()