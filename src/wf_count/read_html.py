from bs4 import BeautifulSoup
import requests


def get_soup(url):
    html_doc = requests.get(url).text
    return BeautifulSoup(html_doc, 'html.parser')


def get_text(url):

    return get_soup(url).get_text()


def save_text(data, filename):

    with open(filename, "w") as fp:
        for line in data:
            fp.write(line)


def save_text_from_html(url, filename):

    save_text(get_text(url), filename)


def get_links_from_main_url(url: str):

    soup = get_soup(url)
    inside_links = set()
    for link in soup.find_all('a'):
        if not link.get('target'):
            if url[-1] == '/':
                if link.get('href')[0] == '/':
                    inside_links.add(f"{url}{link.get('href')[1::]}")
                else:
                    inside_links.add(f"{url}{link.get('href')}")
            else: # url don't have '/' at the and
                if link.get('href')[0] == '/':
                    inside_links.add(f"{url}{link.get('href')}")
                else:
                    inside_links.add(f"{url}/{link.get('href')}")
    return inside_links
