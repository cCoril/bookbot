test = "books/frankenstein.txt"

def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    counter = 0
    for word in words:
        counter += 1
    return counter


def get_num_chars(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.lower()
    count = {}
    for char in words:
        if char.isalpha():
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
        result = {"char": f"{char}", "num": num}
        c_list.append(result)
    return c_list


def sort_on(chars):
    return chars["num"]


def sort_list(file_path):
    chars = get_org_dict(file_path)
    chars.sort(reverse=True, key=sort_on)
    return chars

