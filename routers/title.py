from fastapi import Path, APIRouter, HTTPException
from starlette import status
from bs4 import BeautifulSoup
from utils.encryptor import encrypt
from utils.html import get_html_document
import re

router = APIRouter()


@router.get("/{search_item}", status_code=status.HTTP_200_OK)
async def get_title(search_item: str = Path(min_length=1)):
    url_to_scrape = "https://kayoanime.com/?s=" + search_item

    html_document = get_html_document(url_to_scrape)

    soup = BeautifulSoup(html_document, 'html.parser')

    h2_tag = soup.find('h2', class_='post-title')
    img_tag = soup.find('img', class_='attachment-jannah-image-large size-jannah-image-large wp-post-image')
    span_tag = soup.find('span', class_="meta-views meta-item very-hot")
    if h2_tag:
        a_tag = h2_tag.find('a', attrs={'href': re.compile("^https://")})
        post_url = encrypt(a_tag.get('href'), key=3)
        title = str(a_tag).split(">")[1][:-3]
        thumb_nail = encrypt(img_tag.get('src'), 3)
        meta_count = span_tag.get_text()
        return {
            'main-title': title,
            'url': post_url,
            'thumbnail': thumb_nail,
            'metaCount': meta_count,
        }
    else:
        return HTTPException(status_code=404, detail="Item Not Found")
