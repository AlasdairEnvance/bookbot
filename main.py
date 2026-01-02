def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

if __name__ == "__main__":
    main()
