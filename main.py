

def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["count"]


def char_count_sort(char_count):
    sorted_list = []
    for letter in char_count:
        sorted_list.append({"letter": letter, "count": char_count[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_char_count(text):
    chars = {}
    for letter in text:
        lower = letter.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)

    num_words = get_num_words(text)
    char_count = get_char_count(text)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")

    
    char_count_sorted = char_count_sort(char_count)

    for item in char_count_sorted:
        if not item["letter"].isalpha():
            continue
        print(f"The '{item['letter']}' character was found {item['count']} times")

    print("--- End report ---")


main()
