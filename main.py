from stats import get_num_words

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file: # for windows compatibility
        return file.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    
    get_num_words(text)



main()
