import sys
print(sys.argv)
from stats import count_words, count_character_frequency, sort_dict


def get_book_text(fpath):
    with open(fpath) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    n_words = count_words(text)
    char_freq = count_character_frequency(text)
    dict_list = sort_dict(char_freq)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {n_words} total words")
    print("--------- Character Count -------")
    for d in dict_list:
        if d['char'].isalpha():
            print(f"{d['char']}: {d['num']}")
        continue
    print("============= END ===============")


if __name__ == "__main__":
    main()
