import json
import os

import requests

MASHAPE_KEY = os.getenv('SECRET_KEY')


def get_domain_status(domain):
    url = "https://domainr.p.rapidapi.com/v2/status"
    querystring = {"mashape-key": f"{MASHAPE_KEY}", "domain": f"{domain}"}
    headers = {
        "X-RapidAPI-Key": f"ff06b00acdmsh4fe55ffe0bcc175p1f2011jsnc2056bdbf001",
        "X-RapidAPI-Host": "domainr.p.rapidapi.com"
    }
    response_json = requests.get(url, headers=headers, params=querystring)
    response = json.loads(response_json.text)
    return response


