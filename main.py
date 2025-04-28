import sys
from stats import get_num_words
from stats import characters_from_book
from stats import chars_dict_to_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    wc = get_num_words(sys.argv[1])
    char = chars_dict_to_sorted_list(characters_from_book(sys.argv[1]))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for item in char:
        character = item["char"]
        if character.isalpha():
            print(f"{character}: {item['num']}")
    print("============= END ===============")
