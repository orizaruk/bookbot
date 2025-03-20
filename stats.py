from typing import List
from collections import defaultdict

# takes in a string and returns the number of words inside of that string
def get_num_words(text: str) -> int:
    return len(text.split())

# takes a string and returns a dictionary where each character is a key and the value is the number of times
# it shows up in the string
def get_char_count(text: str) -> defaultdict:
    char_count = defaultdict(int)
    for char in text:
        char_count[char.lower()] += 1
    return char_count

# takes a dictionary from the type returned by the get_char_count function and sorts it in reverse order
def sort_count_dict(char_count: defaultdict) -> List:
    dicts_list = []

    for key, value in char_count.items():
        dicts_list.append({"character": key, "count": value})

    dicts_list.sort(reverse=True, key=lambda char_dict: char_dict["count"])

    return dicts_list
