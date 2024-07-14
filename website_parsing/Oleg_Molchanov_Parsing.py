# -------------------------------------------- 00 Подготовка --------------------------------------------
""" Подготовка и установка  """
# -------------------------------- 01 Введение. Базовый пример работы с BeautifulSoup --------------------------------

import re
import requests
import csv
from bs4 import BeautifulSoup

def get_html_1(url):  # <- url - это ссылка на сайт  | <- Получение html документа
    respons = requests.get(url)  # <- respons - это ответ сервера | get - получение
    return respons.text


def get_date_1(html):  # <- Получение данных c html документа
    soup = BeautifulSoup(html, 'lxml')  # <- Создание экземляра класса BeautifulSoup
    h1 = soup.find('div', id='home-welcom').find('header').find('h1').text
    return h1


def main_1():
    url = 'https://ru.wordpress.org/'  # <- переменная url со ссылкой на нужный сайт
    print(get_date_1(get_html_1(url)))  # <- получение ответа сервера


if __name__ == '__main__':  # <- Проверка на то, что файл был запущен из основного файла
    main_1()


# ------------------------------- 02 Парсинг множественных данных и экспорт в csv-файл -------------------------------


def get_html_2(url):
    respons = requests.get(url)
    return respons.text


def refind_1(s):
    rating = s.split(' ')[0]

    return rating.replace(',', '')


def write_csv_1(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'], data['url'], data['reviews']))


def get_data_2(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[1]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h2').text
        url_plugin = plugin.find('h2').find('a').get('href')
        full_rating = plugin.find('span', class_='rating-count').find('a').text
        refind_rating = refind_1(full_rating)

        data = {'name': name,
                'url': url_plugin,
                'reviews': refind_rating}

        write_csv_1(data)

    return popular


def main_2():
    url = 'https://wordpress.org/plugins/'
    get_data_2(get_html_2(url))


if __name__ == '__main__':
    main_2()


# ------------------------------- 03 Парсинг табличных данных -------------------------------
def get_html_3(url):
    respons = requests.get(url)
    return respons.text


def write_csv_2(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['symbol'],
                         data['url'],
                         data['price']))


def get_page_data_1(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='currencies').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        name = tds[1].find('a', class_='currency-name-container').text
        symbol = tds[1].find('a').text
        url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
        price = tds[3].find('a').get('data-usd')
        data = {'name': name,
                'symbol': symbol,
                'url': url,
                'price': price}

        write_csv_1(data)


def main_3():
    url = 'https://coinmarketcap.com/'
    get_page_data_1(get_html_3(url))


if __name__ == '__main__':
    main_3()


# ------------------------------- 04.1 Работа с пагинацией сайтов (метод 1) -------------------------------

def get_html_4(url):
    respons = requests.get(url)
    if respons.ok:
        return respons.text
    else:
        print(respons.status_code)


def refine_cy_1(s):
    return s.split(' ')[-1]


def write_csv_3(data):
    with open('yaca.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['snippet'],
                         data['cy']))


def get_page_data_2(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', class_='yaca-snippet')

    for li in lis:
        try:
            name = li.find('h2').text
        except:
            name = ''

        try:
            url = li.find('h2').find('a').get('href')
        except:
            url = ''

        try:
            snippet = li.find('div', class_='yaca-snippet__text').text.strip()
        except:
            snippet = ''

        try:
            c = li.find('div', class_='yaca-snipper__cy').text.strip()
            cy = refine_cy_1(c)
        except:
            cy = ''

        data = {'name': name,
                'url': url,
                'snippet': snippet,
                'cy': cy}

        write_csv_3(data)


def main_4():
    pattern = '...url...{}.html'
    for i in range(0, 5):
        url = pattern.format(str(i))
        get_page_data_2(get_html_4(url))


if __name__ == '__main__':
    main_4()


# ------------------------------- 04.2 Работа с пагинацией сайтов (метод 2) -------------------------------
#     url = 'https://coinmarketcap.com/'


def get_html_5(url):
    respons = requests.get(url)
    if respons.ok:
        return respons.text
    print(respons.status_code)


def write_csv_4(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['url'], data['price']))


def get_page_data_3(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='currencies').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        try:
            name = tds[1].find('a', class_='currency-name-container').text.strip()
        except:
            name = ''

        try:
            url = 'https://coinmarketcap.com' + tds[1].find('a', class_='currency-name-container').get('href')
        except:
            url = ''

        try:
            price = tds[3].find('a').get('data-usd').strip()
        except:
            price = ''

        data = {'name': name,
                'url': url,
                'price': price}

        write_csv_4(data)



def main_5():
    url = 'https://coinmarketcap.com/'
    while True:
        get_page_data_3(get_html_5(url))
        soup = BeautifulSoup(get_html_5(url), 'lxml')
        try:
            pattern = 'Next'
            url = 'https://coinmarketcap.com/' + soup.find('ul',
                  class_='pagination').find('a', text=re.compile(pattern)).get('href')
        except:
            break


if __name__ == '__main__':
    main_5()

# ------------------------------- 05 Чтение и запись данных в csv-файлы -------------------------------


def write_csv_5(data: dict):
    with open('names.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['surname'], data['age']))


def write_csv_6(data: dict):
    with open('names_2.csv', 'a') as file:
        order = ['name', 'surname', 'age']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def main_6():
    d1 = {
        'name': 'Petr',
        'surname': 'Ivanov',
        'age': 21,
    }

    d2 = {
        'name': 'Ivan',
        'surname': 'Ivanov',
        'age': 18,
    }

    d3 = {
        'name': 'Ksu',
        'surname': 'Petrova',
        'age': 32,
    }

    l = [d1, d2, d3]

    with open('cmc.csv') as file:
        fieldnames = ['name', 'url', 'price']
        reader = csv.DictReader(file, fieldnames=fieldnames)
        for row in reader:
            print(row)

    # for i in l:
    #     write_csv_5(i)


if __name__ == '__main__':
    main_6()

# ----------------------------- 06 Продвинутые приемы работы с библиотекой BeautifulSoup -----------------------------
# .find()
# .find_all()

# .parent
# .find_parent()

# .parents
# .find_parents()

# .find_next_sibling()
# .find_previous_sibling()

def get_copywriter(tag):
    whois = tag.find('div', id='whois').text.strip()
    if 'Copywriter' in whois:
        return tag
    return None


def get_salary(s):
    # salary: 2700 usd per month
    pattern = r'\d{1,9}'
    salary = re.findall(pattern, s)[0]
    print(salary)


def main_7():
    file = open('index.html').read()
    soup = BeautifulSoup(file, 'lxml')
    # row = soup.find_all('div', {'data-set': 'salary'})
    #
    # alena = soup.find('div', text='Alena').find_parent(class_='row')
    # print(alena)

    # copywriters = []
    #
    # persons = soup.find_all('div', class_='row')
    # for person in persons:
    #     cw = get_copywriter(person)
    #     if cw:
    #         copywriters.append(cw)
    #
    # print(copywriters)

    salary = soup.find_all('div', text=re.compile('\d{1,9}'))
    for i in salary:
        print(i.text)

    # ^ - начало строки
    # $ - конец строки
    # . - любой символ
    # + - неограниченное количество вхождений
    # '\d' - цифра
    # '\w' - буквы, цифры, _



if __name__ == '__main__':
    main_7()

