from collections import defaultdict

def word_counter(book_string):
    book_array = book_string.split()
    num_words = len(book_array)
    return num_words

def count_characters(book_string):
    book_string = book_string.lower()
    character_counter_dict = defaultdict(int)
    for char in book_string:
        character_counter_dict[char] += 1
    return character_counter_dict

def sort_dictionary(dict):
    sorted_list_of_dictionaries = []

    for (k,v) in dict.items():
        sorted_list_of_dictionaries.append({"char" : k, "num" : v})
    sorted_list = sorted(sorted_list_of_dictionaries, key = lambda d : d["num"], reverse = True)
    return sorted_list

    
