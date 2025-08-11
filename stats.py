def number_of_words(text_of_book):
    words = len(text_of_book.split())
    return words

def number_of_each_letter(text_of_book):
    lowercase = text_of_book.lower()
    each_letter = {}
    for letter in lowercase:
        each_letter[letter] = each_letter.get(letter, 0) +1
    return each_letter

def sort_on(on):
    return on["num"]

def sorted_dictionary(each_letter):
    sorted_dict = []
    for char in each_letter:
        sorted_dict.append({"char": char, "num": each_letter[char]})
        sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict