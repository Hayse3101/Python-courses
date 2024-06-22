# -------------------------------------------- 00 Подготовка --------------------------------------------
""" Подготовка и установка  """
# -------------------------------- 01 Введение. Базовый пример работы с BeautifulSoup --------------------------------

import requests
from bs4 import BeautifulSoup


def get_html(url):  # <- url - это ссылка на сайт  | <- Получение html документа
    respons = requests.get(url)  # <- respons - это ответ сервера | get - получение
    return respons.text


def get_date(html):  # <- Получение данных c html документа
    soup = BeautifulSoup(html, 'lxml')  # <- Создание экземляра класса BeautifulSoup
    h1 = soup.find()


def main():
    url = 'https://ru.wordpress.org/'  # <- переменная url со ссылкой на нужный сайт
    print(get_html(url))  # <- получение ответа сервера


if __name__ == '__main__':  # <- Проверка на то, что файл был запущен из основного файла
    main()
