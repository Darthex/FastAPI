import requests


def get_html_document(url):
    response = requests.get(url)
    return response.text
