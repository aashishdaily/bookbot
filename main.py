import sys

from stats import count_words, count_characters, sorting

        
def main():
    """
    calls and prints get_book_text
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_counts = count_words(text)
    characters = count_characters(text)
    sorted_characters = sorting(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counts} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_characters:
        if char_dict["char"].isalpha():
        # print this character and its count
            print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ===============")


def get_book_text(filepath):
    """
    takes filepath reads returns string
    """
    with open(filepath) as f:
        return f.read()    


main()