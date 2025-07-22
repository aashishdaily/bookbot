def count_words(texts: str):
    words = texts.split()
    return len(words)


def count_characters(texts: str):
    unique_characters = {}

    for words in texts:
        for word in words.lower():
            unique_characters[word] = unique_characters.get(word, 0) + 1

    return unique_characters



def sorting(characters_dict: dict):
    filtered_items = []

    for key, value in characters_dict.items():
        valuess = {"char": key, "num": value}
        filtered_items.append(valuess)
    
    filtered_items.sort(key=lambda item: item["num"], reverse=True)
    return filtered_items