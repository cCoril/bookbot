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

def get_org_dict(file_path):
    dict = get_num_chars(file_path)
    c_list = []
    for char in dict:
        num = dict[char]
        result = {"char": char, "num": num}
        c_list.append(result)
    return c_list

def sort_on(chars):
    return chars["num"]

def sort_list(file_path):
    chars = get_org_dict(file_path)

    chars.sort(reverse=True, key=sort_on)
    print(chars)

print(get_org_dict(test))

# result = {f"char:{char}, num: {num}"}