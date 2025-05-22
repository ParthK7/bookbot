def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def word_counter(book_string):
    book_array = book_string.split()
    num_words = len(book_array)
    print (f"{num_words} words found in the document")

def main():
    path = 'books/frankenstein.txt'
    entire_book = get_book_text(path)
    word_counter(entire_book)

main()