import requests
from fastapi import APIRouter
from starlette import status
from routers.title import get_title
from routers.content import get_content

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
async def get_recommendations():
    url = "https://anime-db.p.rapidapi.com/anime"

    querystring = {"page": "1", "size": "10", "sortBy": "ranking", "sortOrder": "asc"}

    headers = {
        "X-RapidAPI-Key": "2c5ffafad3msheaf63ada2e54a71p122146jsnfa80303c4eab",
        "X-RapidAPI-Host": "anime-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


@router.get('/select', status_code=status.HTTP_200_OK)
def select_recommendation(search_title):
    res = get_title(search_title)
    return res
