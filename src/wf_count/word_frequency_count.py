from collections import Counter


FIRST_SYMBOL_OF_VARIABLE_NAME = r"_*#$"
MINIMUM_WORD_LENGTH = 2


lowercase_first_char = lambda string: string[:1].lower() + string[1:] if string else ''


is_hyphen_in_string = lambda string: True if string.find("-") >= 0 else False


def count_words(text: str) -> Counter:
    """
    The function takes a string and returns a Counter object that maps words to their counts.

    :param text: string
    :return: the Counter object
    """
    clear_words = []
    words = text.split()
    for word in words:
        if len(word) < MINIMUM_WORD_LENGTH:
            break
        if word[0] in FIRST_SYMBOL_OF_VARIABLE_NAME:
            break
        if not word[-1].isalpha():
            word = word[: -1]
        if not word[0].isalpha():
            word = word[1:]
        clear_word = lowercase_first_char(word)
        if ((clear_word.isalpha() or is_hyphen_in_string(word))
                and clear_word.islower()):
            clear_words.append(clear_word)
    return Counter(clear_words)
