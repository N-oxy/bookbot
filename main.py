from stats import count_words, count_letters, book_report
import sys

def get_book_text(file_path):
    with open(file_path, encoding='utf-8') as file:
        content = file.read()
    return content

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing the book at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(file_path))} total words")
    print("--------- Character Count -------")
    report = book_report(count_letters(get_book_text(file_path)))
    for entry in report:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()