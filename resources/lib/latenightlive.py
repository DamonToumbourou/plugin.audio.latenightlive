import requests
import re
from bs4 import BeautifulSoup as bs

URL = "http://www.abc.net.au/radionational/programs/latenightlive/"


def get_audio():

    page = requests.get(URL)
    soup = bs(page.text, 'html.parser')

    output = []

    for content in soup.find_all('div', class_="cs-teaser"):
        try: 
            link = content.find('a', {'class': 'ico ico-download'})
            link = link.get('href')
            
            title = content.find('h3', {'class': 'title'})
            title = title.get_text()
            
            desc = content.find('div', {'class': 'summary'})
            desc = desc.get_text()
            desc = desc.split('\n')[1]
            
            thumbnail = content.find('img')
            thumbnail = thumbnail.get('src')

        except AttributeError:
            continue
        
        item = {
                'url': link,
                'title': title,
                'desc': desc,
                'thumbnail': thumbnail
        }
        
        output.append({
            'label': item['title'],
            'thumbnail': item['thumbnail'],
            'path': item['url'],
            'info': item['desc'],
            'is_playable': True,
        })
        
    return output

