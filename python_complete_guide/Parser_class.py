# --------------------------------------------------------------------------
# Lesson 39 ----- Класс парсинга -----

from bs4 import BeautifulSoup
import urllib.request


class Parser:
    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('li', class_='top9__item')

        for item in news:
            """ find возвращает один элемент """
            title = item.find('h3', class_="article-preview__title").get_text()
            print(title)
            desc = item.find('p', class_="article-preview__desc").get_text()
            # desc = None
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(
                    f"Новость №{i}\n\nНазвание: {item['title']}\nОписание: {item['desc']}\nСсылка: {item['href']}\n\n"
                    f"*****************\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
