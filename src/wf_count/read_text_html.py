from bs4 import BeautifulSoup
import requests


def get_soup(url):
    html_doc = requests.get(url).text
    return BeautifulSoup(html_doc, 'html.parser')


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


def get_texts(urls):

    return [get_soup(url).get_text() for url in urls]

