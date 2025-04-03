import os
import read_html
from word_frequency_count import sort_words_into_known_and_unknown


url = "https://python.swaroopch.com/data_structures.html"

filename = os.path.join(os.getcwd(), "data_structures.txt")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # read_html.save_text_from_html(url, filename)
    sort_words_into_known_and_unknown(filename)
