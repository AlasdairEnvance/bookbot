def count_words(text):
    return(len(text.split()))


def count_character_frequency(text):
    text = text.lower()
    count_dict = {}
    for char in text:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict


def sort_on(items):
    return items["num"]


def sort_dict(count_dict):
    dict_list = []
    for char, count in count_dict.items():
        dict_list.append({"char": char, "num": count})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
