import json
import os

import requests

MASHAPE_KEY = os.getenv('SECRET_KEY')


def get_search_info(domain):
    url = "https://domainr.p.rapidapi.com/v2/search"

    querystring = {"mashape-key": f"{MASHAPE_KEY}", "query": f"{domain}", 'registrar': 'ionos.com'}

    headers = {
        "X-RapidAPI-Key": "ff06b00acdmsh4fe55ffe0bcc175p1f2011jsnc2056bdbf001",
        "X-RapidAPI-Host": "domainr.p.rapidapi.com"
    }

    response_json = requests.get(url, headers=headers, params=querystring)
    response = json.loads(response_json.text)
    return response
