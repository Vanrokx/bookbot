import sys
from stats import get_num_words, count_characters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{get_num_words(file_contents)} words found in the document")
    print("")
    
    chars = count_characters(file_contents)
    list_of_chars = list(chars.keys())
    list_of_chars.sort()
    for char in list_of_chars:
        print(f"{char}: {chars[char]}")
    
    print("--- End report ---")




main()
