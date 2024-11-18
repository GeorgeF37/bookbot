def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    the_count = word_counter(text)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{the_count} words found in the document\n")
    letter = letter_counter(text)
    
    sorted_letter = []
    for l in letter:
        if l.isalpha():
            sorted_letter.append({'name':l,'num':letter[l]})
    
    sorted_letter.sort(reverse=True, key=sorter)
    
    for i in sorted_letter:
        print(f"The '{i['name']}' character was found {i['num']} times.")

    print('--- End report ---')


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

def letter_counter(text):
    the_book = text.lower()
    the_letters = {}
    for letter in the_book:
        if letter not in the_letters:
            the_letters.update({letter: 1})
        elif letter in the_letters:
            the_letters[letter] += 1
    return the_letters

def sorter(dict):
    return dict["num"]

main()