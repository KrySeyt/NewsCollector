import time
from datetime import datetime

from collections import defaultdict

import requests
from bs4 import BeautifulSoup, Tag

from DjangoORM.orm import models


DOTA_NEW_URL = r"https://www.cybersport.ru/tags/dota-2/"
RSS_URL: str = r'https://www.cybersport.ru/rss/materials'
IMAGE_HOST: str = r'https://virtus-img.cdnvideo.ru/images/material-card/plain/'
REQUEST_DELAY: int = 15

PROXIES: dict = {}


def get_new_soup(url: str) -> BeautifulSoup:
    time.sleep(REQUEST_DELAY)
    response: requests.Response = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_new_text(soup: BeautifulSoup) -> str:
    frame: Tag = soup.find(class_='text-content js-mediator-article '
                                  'js-mediator-article root_sK2zH content_5HuK5')

    text: str = ""
    for text_block in frame.find_all('p'):
        text += text_block.get_text()
        if text_block.next:
            text += ' '

    return text


def rss_parse(rss_url: str):
    slug_to_category_name: defaultdict = defaultdict(lambda: 'Неизвестно')
    slug_to_category_name['dota-2'] = 'Dota 2'
    slug_to_category_name['cs-go'] = 'CS:GO'
    slug_to_category_name['games'] = 'Игры'

    response: requests.Response = requests.get(rss_url)
    soup: BeautifulSoup = BeautifulSoup(response.text, 'xml')

    counter: int = 0
    for new in soup.find_all('item'):
        if counter >= 5:
            break

        counter += 1

        link: list = new.link.get_text().split('/')

        category_slug: str = link[4]
        category_name: str = slug_to_category_name[category_slug]

        new_title: str = new.title.get_text()
        new_slug: str = link[5]

        soup: BeautifulSoup = get_new_soup(fr"https://www.cybersport.ru/tags/{category_slug}/{new_slug}")
        new_text: str = get_new_text(soup)
        date: datetime = datetime.strptime(new.pubDate.get_text(), '%a, %d %b %y %H:%M:%S %z')
        image_url: str = new.enclosure['url']
        yield {'new_title': new_title, 'new_slug': new_slug, 'new_text': new_text, 'date': date, 'image_url': image_url,
               'category_slug': category_slug, 'category_name': category_name}


def collect_data() -> None:
    for new in rss_parse(RSS_URL):
        if not models.New.objects.filter(slug=new['new_slug']).exists():
            if models.Category.objects.filter(slug=new['category_slug']).exists():
                category: models.Category = models.Category.objects.get(slug=new['category_slug'])
            else:
                category: models.Category = models.Category(
                    slug=new['category_slug'],
                    name=new['category_name']
                )
                category.save()

            models.New.objects.create(
                title=new['new_title'],
                text=new['new_text'],
                slug=new['new_slug'],
                date=new['date'],
                image_url=new['image_url'],
                category=category,
                is_published=True,
                rating=models.Rating.objects.create()
            )


def main():
    while True:
        try:
            collect_data()
        except AttributeError as error:
            print(error)
        finally:
            time.sleep(3600)


if __name__ == '__main__':
    main()
