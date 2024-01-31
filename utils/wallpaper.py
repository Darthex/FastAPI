from utils.html import get_html_document
from bs4 import BeautifulSoup


def get_wallpaper(abc):
    title = 'kimetsu-no-yaiba'
    search = 'https://wallpaperaccess.com/' + title
    print(search)
    html_document = get_html_document(search)

    soup = BeautifulSoup(html_document, 'html.parser')

    tags = soup.find_all('div')
    print(tags)
