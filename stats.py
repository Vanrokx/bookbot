def get_num_words(contents):
    return len(contents.split())

def count_characters(contents):
    characters = {}
    for i in range(0, len(contents)):
        char = contents[i].lower()
        if char in characters:
            characters[char] += 1
        elif char.isalpha():
            characters[char] = 1
    return characters

