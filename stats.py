test = "/home/carlr/workspace/github.com/cCoril/bookbot/books/frankenstein.txt"

def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    counter = 0
    for word in words:
        counter += 1
    return f"{counter} words found in the document"

def get_num_chars(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.lower()
    count = {}
    for char in words:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

print(get_num_chars(test))
