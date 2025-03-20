import sys
from stats import get_num_words, get_char_count, sort_count_dict

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()

def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    loaded_book = get_book_text(book_path)

    # get the relevant information and save it 
    num_words = get_num_words(loaded_book)
    character_count_dict = get_char_count(loaded_book)
    character_count_dict = sort_count_dict(character_count_dict)

    # print in an organized manner all of the information

    print(f"""============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------
    """)

    for ch in character_count_dict:
        if ch["character"].isalpha():
            print(f"{ch["character"]}: {ch["count"]}")
    
    print("============= END ===============")


if __name__ == "__main__":
    main()