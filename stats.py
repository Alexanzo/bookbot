def get_book_text(path):
    file_contents = None
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def sort_on(dict):
    return dict["num"]

def get_num_words(path):
    count = get_book_text(path).split()
    return len(count)

def characters_from_book(path):
    characters = get_book_text(path).lower()
    charact = {}
    for letters in characters:
        if letters in charact:
            charact[letters] = charact[letters] + 1
        else:
            charact[letters] = 1
    return charact

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char,count in char_dict.items():
        sorted_list.append({"char": char,"num": count})
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list