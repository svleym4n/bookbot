def get_num_words(text):

    words = text.split()

    num_words = 0

    for word in words:
        num_words += 1
    
    return print(f"{num_words} words found in the document")