def count_words(text):
    i = 0
    for word in text.split():
        i += 1
    return i

def count_letters(text):

    letters = {}

    for char in text:
        letter = char.lower()
        if letter in letters:
            letters[letter] += 1
        elif letter == " " or letter == "\n" or not letter.isalpha():
            continue
        else:
            letters[letter] = 1

    return letters

def book_report(letters):
    new_letters = []
    for char, count in sorted(letters.items()):
        new_letters.append({"char": char, "num": count})
        new_letters.sort(key=lambda x: x["num"], reverse=True)
    return new_letters