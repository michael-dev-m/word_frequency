
from collections import Counter
from time import time
import os
import json

from word_frequency_count import count_words
from read_text_html import get_links_from_main_url, get_texts
from read_text_pdf import get_text_pdf

I_KNOW = "i_know_words"
I_AM_LEARNING = "i_am_learning_these_words"
I_DO_NOT_KNOW = "i_do_not_know_these_words"
N = 15


def sort_words_into_known_and_unknown(file_name):

    words_all = Counter(load_data_json(file_name))
    i_know_words = load_data_json(I_KNOW)
    i_do_not_know_words = load_data_json(I_DO_NOT_KNOW)
    i_am_learning_words = load_data_json(I_AM_LEARNING)
    words = words_all - Counter(i_know_words) - Counter(i_do_not_know_words) - Counter(i_am_learning_words)
    print(f"{len(words)}")
    for word, count in words.most_common(N):
        answer = input(f"Do you know - {word}? y/n: ")
        if answer == "y" or answer == "Y":
            i_know_words[word] = count
        if answer == "n" or answer == "N":
            i_do_not_know_words[word] = count
        if answer == "exit":
            break
    save_data_json(i_know_words, I_KNOW)
    save_data_json(i_do_not_know_words, I_DO_NOT_KNOW)

    print(f"There are {len(i_do_not_know_words)} unknown words in the list of unknown words.")
    print(f"Wow! You know {len(i_know_words)} words.")


def save_data_json(data, filename):

    with open(f"{filename}.json", 'w') as fp:
        json.dump(data, fp)


def load_data_json(filename):

    with open(f"{filename}.json", 'r') as fp:
        data = json.load(fp)
    return data


def save_data_text(data, filename):

    with open(f"{filename}.txt", "w") as fp:
        for line in data:
            fp.write(line)


def read_data_text(filename):

    with open(f"{filename}.txt", "r") as fp:
        return fp.read()


def get_modified(filename):

    words_from_chapter = load_data_json(filename)
    all_words = load_data_json("python_swaroopch_com")
    result = {}
    for word in words_from_chapter:
        result[word] = all_words[word]
    save_data_json(result, f"{filename}_modified")
    return

url = "https://python.swaroopch.com/modules.html"

# url = "https://www.olx.ua/uk/nedvizhimost/"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # text = get_texts([url])
    # save_data_text(text, "modules_text")

    # get_modified("modules")

    sort_words_into_known_and_unknown("modules_modified")
    # data = read_data_text("modules_text.txt")
    # words = count_words(data)
    # save_data_json(words, "modules")
    # print(words)
    # print(len(words))



