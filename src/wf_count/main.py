import read_html
import word_frequency_count as wfc


url = "https://python.swaroopch.com/data_structures.html"

filename = "data_structures.txt"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # read_html.save_text_from_html(url, filename)
    wfc.sort_words_into_known_and_unknown(filename)
