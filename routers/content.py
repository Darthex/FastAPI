from fastapi import APIRouter
from starlette import status
from bs4 import BeautifulSoup
from utils.encryptor import encrypt, decrypt
from utils.html import get_html_document
import re

router = APIRouter()


@router.get("/links/", status_code=status.HTTP_200_OK)
async def get_content(post_url):
    dec_url = decrypt(post_url, key=3)

    html_document = get_html_document(dec_url.replace('"', '').strip())

    soup = BeautifulSoup(html_document, 'html.parser')

    titles = []
    urls = []
    url_titles = []

    s = str(re.escape('>'))
    es = str(re.escape('<s'))
    e = str(re.escape('<'))

    div_tag = soup.find_all('div', class_='toggle tie-sc-close')

    if div_tag:
        for item in div_tag:
            tags = item.find_all('a', attrs={'href': re.compile("^https://")})
            h3 = item.find_all('h3', class_='toggle-head')

            for x in h3:
                titles.append(re.findall(s + "(.*)" + es, str(item))[0])

            semi_url_list = []
            semi_url_title = []
            for x in tags:
                semi_url_title.append(re.findall(s + "(.*)" + e, str(x)))
                semi_url_list.append(encrypt(x.get('href'), key=3))
            urls.append(semi_url_list)
            url_titles.append(semi_url_title)

        dict_to_return = [{'title': title, 'urls': url_list, 'url_titles': url_title_list} for
                          title, url_list, url_title_list
                          in zip(titles, urls, url_titles)]
        return [dict_to_return, {"isExpandable": True}]

    else:
        for item in soup.find_all('a',
                                  attrs={'href': re.compile(
                                      '|'.join(["^https://drive.google.com", "^https://tinyurl.com"]))}):
            url_titles.append(re.findall(s + "(.*)" + e, str(item)))
            enc_url = encrypt(str(item.get('href')), key=3)
            urls.append(enc_url)

        dict_to_return = [{'url': url_list, 'url_titles': url_title_list} for
                          url_list, url_title_list in zip(urls, url_titles)]

        return [dict_to_return, {"isExpandable": False}]
