from stats import get_num_words

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{get_num_words(file_contents)} words found in the document")
    print("")
    
    chars = count_characters(file_contents)
    list_of_chars = list(chars.keys())
    list_of_chars.sort()
    for char in list_of_chars:
        print(f"The '{char}' character was found {chars[char]} times.")
    
    print("--- End report ---")


def count_characters(contents):
    characters = {}
    for i in range(0, len(contents)):
        char = contents[i].lower()
        if char in characters:
            characters[char] += 1
        elif char.isalpha():
            characters[char] = 1
    return characters



main()
