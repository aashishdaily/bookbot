from stats import count_words, count_characters

        
def main():
    """
    calls and prints get_book_text
    """
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_counts = count_words(text)
    characters = count_characters(text)
    print(f"{word_counts} words found in the document")
    print(characters)


def get_book_text(filepath):
    """
    takes filepath reads returns string
    """
    with open(filepath) as f:
        return f.read()    


main()