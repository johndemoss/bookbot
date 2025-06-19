import sys
from stats import get_word_count, get_char_count, get_sorted_char_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents
    

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    string = get_book_text(sys.argv[1])
    word_count = get_word_count(string)
    char_count = get_char_count(string)
    sorted_char_count = get_sorted_char_count(char_count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for item in sorted_char_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
        

main()