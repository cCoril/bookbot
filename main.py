from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

word_count = get_num_words(sys.argv[1])
characters = get_num_chars(sys.argv[1])
sorted =  sort_list(sys.argv[1])


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for group in sorted:
        print(f"{group['char']}: {group['num']}")
    print("============= END ===============")










main()