import requests
import re
from bs4 import BeautifulSoup as bs

URL = "http://www.abc.net.au/radionational/programs/latenightlive/"


def get_audio():

    page = requests.get(URL)
    soup = bs(page.text, 'html.parser')

    print soup 

    for content in soup.find_all('div', class_="cs-teaser"):
        try: 
            link = content.find('a', {'class': 'ico ico-download'})
            link = link.get('href')
            print link
        
        except AttributeError:
            continue

get_audio()
