import requests
from bs4 import BeautifulSoup
import csv
from django.views.decorators.csrf import csrf_exempt

HOST = 'https://filmix.co/'
URL = 'https://filmix.co/serials/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
CSV = 'shows.csv'


@csrf_exempt
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

@csrf_exempt
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='full')
    show = []

    for item in items:
        show.append(
            {
                'title': item.find('h2', class_='name').get_text(),
                'link_show': HOST + item.find('a', class_='name').find('href'),
                'image': HOST + item.find('a', class_='fancybox').find('img').get('src')
            }
        )
    return show


@csrf_exempt
def parser():
    PAGENATION = input('Pages for parsing: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        show = []
        for page in range(1, PAGENATION):
            print(f'Parsed pages: {page}')
            html = get_html(URL, params={'page': page})
            show.extend(get_content(html.text))
            print(show)

        print('Finished parsing')
    else:
        print('Error parsing')