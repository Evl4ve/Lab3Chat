import re
from  string import ascii_lowercase, ascii_uppercase


ukrainian_lowercase = 'абвгдеєжзишїйклмнопрстуфхцчшщьюя'
ukrainian_uppercase = ukrainian_lowercase.upper()

alphabets = [ascii_lowercase, ascii_uppercase, ukrainian_lowercase, ukrainian_uppercase]


def _split_string_to_text_and_digits(string):
    result = []
    for i in string.split():
        result = [*result, *re.split("(\d+)", i), ""]

    result = [i for i in result if i !=''] # remove trailing whitespace
    return result


def _to_shift_char(char, shift):
    for alphabet in alphabets:
        if (index := alphabet.find(char)) != -1:
            return alphabet[(index + shift) % len(alphabet)]
    return char


def _to_shift_string(string, shift):
    shifted_string = ""

    for i, characters in enumerate(_split_string_to_text_and_digits(string)):
        if characters.isdigit():
            shifted_string += str(int(characters)+shift)
        else:
            for char in characters:
                shifted_string += _to_shift_char(char, shift)
    return shifted_string.rstrip()


def encode(string, shift=1):
    return _to_shift_string(string, shift)


def decode(string, shift=1):
    return _to_shift_string(string, -shift)