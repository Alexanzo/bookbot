def get_book_text(path):
    file_contents = None
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    count = get_book_text("./books/frankenstein.txt").split()
    print(f"{len(count)} words found in the document")

def characters_from_book():
    characters = get_book_text("./books/frankenstein.txt").lower()
    charact = {}
    for letters in characters:
        if letters in charact:
            charact[letters] = charact[letters] + 1
        else:
            charact[letters] = 1
    print(charact)