def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    the_count = word_counter(text)
    print(f"\n{the_count} words in frankenstein.txt\n")
    letter = letter_counter(text)
    print(f"{letter} \n")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    '''counter = 0
    for word in words:
        counter += 1
    print(counter)'''
    return len(words)

def letter_counter(text):
    the_book = text.lower()
    the_letters = {}
    for letter in the_book:
        if letter not in the_letters:
            the_letters.update({letter: + 1})
        elif letter in the_letters:
            the_letters[letter] += 1
    return the_letters

main()