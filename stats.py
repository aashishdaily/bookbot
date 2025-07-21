def count_words(texts: str):
    words = texts.split()
    return len(words)


def count_characters(texts: str):
    unique_characters = {}

    for words in texts:
        for word in words.lower():
            unique_characters[word] = unique_characters.get(word, 0) + 1

    return unique_characters



