def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    path = "books/frankenstein.txt"
    print(get_book_text(path))


main()
