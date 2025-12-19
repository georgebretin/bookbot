def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()

        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters(char_counts):
    # Convert the dictionary to a list of {"char": x, "num": y} dictionaries
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

        # Helper function to use as the sort key
    def sort_key(item):
        return item["num"]
    
    # Sort the list in descending order based on the count
    char_list.sort(key=sort_key, reverse=True)

    return char_list