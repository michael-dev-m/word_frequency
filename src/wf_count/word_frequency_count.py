from collections import Counter
import json
import os


FIRST_SYMBOL_OF_VARIABLE_NAME = r"_*#$"
MINIMUM_WORD_LENGTH = 2
N = 3
I_KNOW = "i_know_these_words.json"
I_AM_LEARNING = "i_am_learning_these_words.json"
I_DO_NOT_KNOW = "i_do_not_know_these_words.json"
MAIN_DICTIONARY = "python_swaroopch_com.json"


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
            continue
        if word[0] in FIRST_SYMBOL_OF_VARIABLE_NAME:
            continue
        if not word[-1].isalpha():
            word = word[: -1]
        if not word[0].isalpha():
            word = word[1:]
        clear_word = lowercase_first_char(word)
        if clear_word.isalpha() and clear_word.islower():
            clear_words.append(clear_word)
            continue
        if is_hyphen_in_string(word):
            parts = word.split("-")
            if all(part.isalpha() and part.islower() for part in parts):
                clear_words.append(clear_word)
    return Counter(clear_words)


def save_data(data, filename):

    with open(filename,  'w') as fp:
        json.dump(data, fp)


def load_data(filename):

    with open(filename,  'r') as fp:
        data = json.load(fp)
    return data


def load_text(filename):

    with open(filename, "r") as fp:
        return fp.read()


def sort_words_into_known_and_unknown(file_name):

    words_from_text = count_words(load_text(os.path.join(os.getcwd(), file_name)))
    i_know_words = load_data(os.path.join(os.getcwd(), I_KNOW))
    i_do_not_know_words = load_data(os.path.join(os.getcwd(), I_DO_NOT_KNOW))
    i_am_learning_words = load_data(os.path.join(os.getcwd(), I_AM_LEARNING))
    words = words_from_text - Counter(i_know_words) - Counter(i_do_not_know_words) - Counter(i_am_learning_words)
    print(f"{len(words)}")
    for word, count in words.most_common(N):
        answer = input(f"{count}  Do you know - {word}? y/n: ")
        if answer == "y" or answer == "Y":
            i_know_words[word] = count
        if answer == "n" or answer == "N":
            i_do_not_know_words[word] = count
        if answer == "exit":
            break
    save_data(i_know_words, os.path.join(os.getcwd(), I_KNOW))
    save_data(i_do_not_know_words, os.path.join(os.getcwd(), I_DO_NOT_KNOW))

    print(f"There are {len(i_do_not_know_words)} unknown words in the list of unknown words.")
    print(f"Wow! You know {len(i_know_words)} words.")
