import bs4
import requests

__KOKA_URL = 'http://www.koka36.de/neu_im_vorverkauf.php'


def get_feed():
    """Get events from Koka36 website"""
    html = requests.get(__KOKA_URL)
    soup = bs4.BeautifulSoup(html.text, 'lxml')

    items = []

    for event in soup.find_all('div', {'class': 'event_box'}):

        data = event.find('div', {'style': 'imagefield'})

        title = data.find('p').string
        description = data.find_all('div')[-1].string
        image = data.find('img').get('src')
        link = event.find('a').get('href')

        if title:
            items.append({
                'title': title,
                'description': description,
                'image': image,
                'link': link
            })

    return items
