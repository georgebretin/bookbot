from stats import count_words, count_characters, sort_characters
import sys


def main():
    # VALIDATE CLI ARGS
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    with open(book_path) as f:
        text = f.read()

    # WORD COUNT
    print("----------- Word Count ----------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")

    # CHARACTER COUNT
    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    for item in sorted_chars:
        char = item["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {item['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
