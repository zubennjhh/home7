import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://ru.sputnik.kg'

HEADERS = {
    'аccept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='list__item  ')
    kg_news = []

    for item in items:
        kg_news.append(
            {
            'title_url': URL + item.find('a').get('href'),
            'title_text': item.find('a', class_='list__title').get_text(),
            'image': URL + item.find('div', class_='list__image').find('img').get('src'),
            'create_data': item.find('div', class_='list__date ').find('span').text,
            'tag': item.find('div', class_='list__controls').find('ul').get_tag('li'),
            })

    return kg_news


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        kg_news1 = []
        for page in range(0, 1):
            html = get_html(f'https://ru.sputnik.kg/news/', params=page)
            kg_news1.extend(get_data(html.text))
            try:
                continue
            except UnicodeEncodeError:
                print(page.encode('utf-8'))
            return kg_news1
        #print(f'\n{kg_news1}\n')
    else:
        raise Exception('Parse Error......')