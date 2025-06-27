from stats import get_num_words, get_num_chars

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

test = "/home/carlr/workspace/github.com/cCoril/bookbot/books/frankenstein.txt"
word_count = get_num_words(test)
characters = get_num_chars(test)

def main():
    # print(get_book_text("/home/carlr/workspace/github.com/cCoril/bookbot/books/frankenstein.txt"))
    print(word_count, characters)

main()