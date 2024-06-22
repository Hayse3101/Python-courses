import os
# from random import randint
# import random as r
# from random import *
import random
import libs

# Это тут так, пусть будет
name = input("g: ")

match name:
    case "Jhon":
        print(f"Hello Jhon")
    case "Artem":
        print("Hello Artem")

match sign_input := input("Введите знак операции: "):
    case '+':
        print("Знак операции +")
    case '-':
        print("Знак операции -")
    case '*':
        print("Знак операции *")
    case '/':
        print("Знак операции /")
    case _:
        print("Не понятно")

# --------------------------------------------------------------------------
# Lesson 4

# Текст коментария
print("Hello, World!")
print("Hello, World !!!")

"""
Многострочный
комнетарий
"""

# --------------------------------------------------------------------------
# Lesson 5

print(1 + 2)  # 3
print(6 - 2)  # 4
print(1 - 2)  # -1
print(9 / 3)  # 3
print(9 % 3)  # 0
print(9 % 4)  # 1
print(12 // 4)  # 3
print(12 // 2)  # 6
print(-3 - 5)  # - 8
print(2 ** 2)  # 4
print(25 ** 0.5)  # 5
print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
print(0.5 + 2)  # 2.5

# --------------------------------------------------------------------------
# Lesson 6

x = 1  # Переменной X присвоено значение 1
y = 1
my_var1 = 50
_my_var1 = 100
# 1my_var = 200 <- не допускается

print(type(x))
print(type(y))

TEST = 20  # <- Константа

# --------------------------------------------------------------------------
# Lesson 7

# test = None
# test = 123

x, y = 3, 5
print(x, y)

my_true = True
my_false = False
print(type(my_true))
print(type(my_false))

# str() int() float () bool()

x = 5.2
print(x, type(x))
x = int(x)
print(x, type(x))
x = str(x)
print(x, type(x))
bool_value = 0
bool_value = bool(bool_value)
print(bool_value, type(bool_value))

# --------------------------------------------------------------------------
# Lesson 8

words = "Hello, \n\"test\", 'World'!"
print(words)

verse1 = 'Всё тихо - полна луна' \
         'Блестит меж вётел над прудом' \
         'И возле берега волна' \
         'С холодным резвистом лучом.'

verse2 = ('Всё тихо - полна луна\n'
          'Блестит меж влётел над прудом\n'
          'И возле берега волна\n'
          'Схолодным резвистом лучом\n')

verse3 = """ Всё тихо - полна луна
             Блестит меж влётел над прудом
             ...
         """

print(verse1)
print(verse2)

# --------------------------------------------------------------------------
# Lesson 9

s = r'C:\d\new.txt'  # <- Срыая строка
print(s)

# s = 'Py' 'thon'
# print(s)

s1 = "Hello, "
s2 = "World!"
s3 = s1 + s2
print(s3)

name = "Jhon"
age = 20
print('My name is' + name + 'I\'m ' + str(age))
print('Hi ' * 5)

s4 = 'Hello, World!'
print(s4[0])  # H
print(s4[-1])  # !

# Срезы - [X - Начало среза: Y - Окончание среза: Z - Шаг среза]
print(s4[0:12])  # Hello, World!
print(s4[-1])  # !
print(s4[0:5])  # Hello
print(s4[:5])  # Hello
print(s4[6:])  # World!
print(s4[::2])  # Hlo ol!
print(s4[::-1])  # !dlroW ,olleH
print(s4[:5] + s4[6:])  # 'HelloWorld!'

# --------------------------------------------------------------------------
# Lesson 10

s6 = 'Hello'
s7 = 'hello'
s8 = 'Hello World'
ns1 = '123'

print(len(s6))  # 5
print(s7.capitalize())  # Hello
print(s6.center(5, '*'))  # *****Hello*****
print(s6.count('l'))  # 2
print(s6.find('o'))  # 4
print(s6.find('t'))  # -1
print(s6.replace('l', 't'))  # hetto
print(s8.split())  # ['hello', 'world']
print(s6.isdigit())  # Fasle
print(ns1.isdigit())  # True
print(s6.isalpha())  # True
print(s8.isalpha())  # False

# --------------------------------------------------------------------------
# Lesson 11

name1 = 'Jhon'
age1 = 30

print('My name is ' + name1 + '. I\'m ' + str(age1))  # My name is Jhon. I'm 30
print('My name is %(name)s. I\'m %(age)d' % {'name': name, 'age': age})  # My name is Jhon. I'm 30
print('My name is %s. I\'m %d' % (name1, age1))  # My name is Jhon. I'm 30
print('My name is {}. I\'m {}'.format(name, age))  # My name is Jhon. I'm 30
print('My name is {0}. I\'m {1}'.format(name, age))  # My name is Jhon. I'm 30
print('My name is {name}. I\'m {age}'.format(name=name, age=age))  # My name is Jhon. I'm 30
print(f'My name is {name}. I\'m {age}')  # My name is Jhon. I'm 30

# --------------------------------------------------------------------------
# Lesson 12

print(2 > 3)  # False
print(2 < 3)  # True
print(2 > 2)  # False
print(2 >= 2)  # True
print(3 == 3)  # True
print(3 != 4)  # True

'''
if выражение1:
    блок кода1
elif выражение2:
    блок кода2
else:
    блок кода3
'''

x = 0
if x:  # <- 0 = False
    print("True")
else:
    print("False")  # <-

# -----

light = 'red'
if light == 'red':  # red = red
    print('Stop')  # <-
elif light == 'yellow':
    print('Waite')
elif light == 'green':
    print('Go')
else:
    print("What?")

# -----

age_user = int(input("Сколько вам лет? "))
if age_user >= 18:
    print("Добро пожаловать!")
else:
    print("Доступ закрыт!")
    print()
    print(f"Так как вам не исполнилость 18! Для этого вам нужно подождать ещё {18 - age_user} лет/год")

# -----

time = 11
day = 'st'

if time > 8 and day != 'su':  # 11 > 8 и st != su
    print("Открыто!")  # <-
else:
    print("Закрыто")

# -----

x = 1
if not x:  # <- 1 а должно быть 0
    print("Ok")
else:
    print("No")  # <-
# -----

x = 1
res = 'Ok' if x else 'No'
print(res)  # Ok

# --------------------------------------------------------------------------
# Lesson 13
'''
while stmt:
    do ...
'''
# while True:
#     print("Test")

# -----

i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

# -----

s = 'Hello, World!'
for i in s:
    if i == ' ':
        continue
    print(f"'{i}'", end=" ")
else:
    print("Gggg")

# -----

for i in 'Hello, World!':
    if i == ",":
        break
    print(i, end=" ")
else:
    print("Gggg")

# --------------------------------------------------------------------------
# Lesson 14

list_value1 = [1, 2, 3, 4, 5, 'hello', [1, 2, '1'], 7]
print(list_value1, type(list_value1))

list_value2 = list('hello')
print(list_value2)

# -----

list_1 = [i for i in 'hello']
print(list_1)
list_2 = [i*2 for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]

print(list(range(1, 11, 2)))  # range(старт, стоп, шаг)

# -----

for i in range(1, 3):
    print(f"Внещний цикл №{i}")
    for j in range(1, 3):
        print(f"\tВнутренний цикл №{j}")

# --------------------------------------------------------------------------
# Lesson 15 ----- дз -----

print("\nТаблица умножения\n\n")

for i in range(1, 10):
    for j in range(2, 10):
        print(f"{i} * {j} = {i * j}\t", end='')
    print()
else:
    print('Well done')

# --------------------------------------------------------------------------
# Lesson 16 ----- Методы для работы со списками -----

list_value2 = [1, 2, 3, 4, 5, 'hello', [1, 2, '1'], 7]
names = ['Ivanov', 'Petrov', 'Sidorov']

list_3 = [1, 2, 3,]
list_4 = ['one', 'two', 'three']

print(names[1])  # <- 2
print(names[6][1])  # <- [1, 2, '1'] <- 2
print(names[:4])  # <- [1, 2, 3, 4]
names[1] = 'Artem'  # <- ['Ivanov', 'Artem', 'Sidorov']
list_value2[2:5] = [10, 20, 30]  # <- [1, 2, 10, 20, 20, 'hello', [1, 2, '1'], 7]
list_value2.append('python')  # <- [1, 2, 3, 4, 5, 'hello', [1, 2, '1'], 7, 'python']
list_3.extend(list_4)  # <- [1, 2, 3, 'one', 'two', 'three']
list_value2.insert(5, 6)  # [1, 2, 3, 4, 5, 6, 'hello', [1, 2, '1'], 7]
list_value2.remove(3)  # <- [1, 2, 4, 5, 'hello', [1, 2, '1'], 7]
names.pop(1)  # <- ['Ivanov', 'Sidorov']
name4 = names.pop(0)  # <- 'Ivanov'

# --------------------------------------------------------------------------
# Lesson 17 ----- Изменяемые и неизменяемые люъекты -----

int_value = 10  # <- Число не изменяемый объект
print(f"{int_value}, id - {id(int_value)})")
int_value = 20  # <- Пересоздали объект
print(f"{int_value}, id - {id(int_value)})")  # <- id будет другое

str_value = 'Hello'  # <- Строка не изменяемый объект
print(f"{str_value}, id - {id(str_value)})")
str_value += 'Python'  # <- Пересоздали объект
print(f"{str_value}, id - {id(str_value)})")  # <- id будет другое

list_value4 = [1, 2, 3]  # <- Списки изменяемые
print(f"{list_value4}, id - {id(list_value4)}")
list_value4[0] = 10  # <- Объект пересоздаваться не будет
list_value4.append(10)  # <- Объект пересоздаваться не будет
print(f"{list_value4}, id - {id(list_value4)}")  # <- id не изменился

# --------------------------------------------------------------------------
# Lesson 18 ----- дз -----

""" Задача 1.1 """
list_value5 = [1, 2, 3]
for i in range(len(list_value5)):
    list_value5[i] *= 2

print(f"Полученный результат списка: {list_value5}")

""" Задача 1.2 """
list_value5 = [1, 2, 3]
list_value6 = [i * 2 for i in list_value5]
print(f"Полученный результат списка: {list_value5}")

# -----

""" Задача 2.1 """
list_value5 = [1, 2, 3]
sum_value = 0
for i in range(len(list_value5)):
    sum_value += list_value5[i] ** 2

print(f"Полученный результат: {sum_value}")

# -----

""" Задача 3.1 """
time_value = int(input("Сколько часов: "))
litres = time_value * 0.5
print(f"Сколько литров нужно выпить: {litres}")

""" Задача 3.2 """
time_value = int(input("Сколько часов: "))
print(f"Сколько литров нужно выпить: {time_value // 2}")

# -----

""" Задача 4 """
str_value = 'Hello World'
if ' ' in str_value:
    str_value.upper()
else:
    str_value.lower()

# --------------------------------------------------------------------------
# Lesson 19 ----- Решение домашнего задания -----
""" Всё решено верно """
# --------------------------------------------------------------------------
# Lesson 20 ----- Кортежи -----

t1 = (1, 2, 3, 4, 5)  # <- Кортеж
t2 = (6, 7, 8, 9, 10)  # <- Кортеж, упаковка кортежа
t3 = tuple((1, 2, 3, 4, 4, 4, 5))  # <- Кортеж
t4 = ()  # <- Пустой кортеж
t5 = tuple("hello")
t6 = t1 + t2
t7 = (1, 2, 3, [4, 5, 6], 7, 8, 9, ['hello', 'world'])
t8 = (1, 2, 3, 4, 5)
t9 = (1, 2, 3)

x1 = t9[0]
y1 = t9[1]
z1 = t9[2]

x2, y2, z2 = t9  # <- Распаковка кортежа

# t7[0] = 1  # <- Error
t7[3][1] = 10  # <- 1, 2, 3, [4, 10, 6], 7, 8, 9, ['hello', 'world']
print(t5)  # <- ('h', 'e', 'l', 'l', 'o')
print(t5[3])  # <- 'l'
print(t6)  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(len(t6))  # 10
print(t3.count(4))  # <- 3
print(t6.index(4))  # <- 3

for i in t5:
    print(i, end=" ")  # <- h e l l o

# --------------------------------------------------------------------------
# Lesson 21 ----- Решение домашнего задания -----

""" Задача 1.1 """

words = ['мадам', 'топот', 'test', 'madam', 'word']
new_words = []

for word in words:
    if word == word[::-1]:
        new_words.append(word)

print(f"Новый список слов: {new_words}")

""" Задача 1.2 """

new_words = [word for word in words if word == word[::-1]]
print(f"Новый список слов: {new_words}")

""" Задача 2.1 """
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
palindromes = []

for str_value in my_str:
    word_r = str_value.replace(' ', '').lower()
    if word_r == word_r[::-1]:
        palindromes.append(word_r)

print(f"Новый список слов: {new_words}")

# ----- Метод .join()

l21_1 = list(range(1, 10))
l21_2 = list('Hello')

s21_1 = '-'.join(map(str, l21_1))
s21_2 = '*'.join(l21_2)

print(s21_1)  # <- 1-2-3-4-5-6-7-8-9
print(s21_2)  # <- H*e*l*l*o

# --------------------------------------------------------------------------
# Lesson 22 ----- Множества -----

set_22_1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
set_22_2 = set('hello')
set_22_3 = {i for i in range(1, 11)}
set_22_4 = {5, 3, 10, 1, 9, 2}
set_22_5 = set()

set_22_a = set('abracadabra')
set_22_b = set('alacazam')
set_22_c = set_22_a - set_22_b  # <- вычитание - убираем из A все буквы, котореы есть в B
set_22_d = set_22_a | set_22_b  # <- объединение - буквы или B A, или A B
set_22_e = set_22_a & set_22_b  # <- пересечение - буквы и B A, и A B
set_22_f = set_22_a ^ set_22_b  # <- множество из элементов - буквы B A или B, но и не в обоих

print(f"{set_22_a} {set_22_b} {set_22_c} {set_22_d} {set_22_e} {set_22_f}", sep='\n')

set_22_6 = set_22_1.copy()  # <-возвращает копию множества
set_22_1.add('t')  # <- Добовляет элемент в множество
set_22_1.remove('t')  # <- удаляет элемент из множества
set_22_3.discard(4)  # <- удаляет элемент, если он находится в множестве
set_22_7 = set_22_1.pop()  # <- Возращает и удаляет первый элемент множества
set_22_4.clear()  # <- Очистка множества

fset_22_1 = frozenset('hello')  # <- frozenset это то же самое множество, только не изменяемое

print(f"{set_22_1} - {type(set_22_1)}")  # <- {'pear', 'banana', 'apple', 'orange'}
print(set_22_2)  # <- {'l', 'h', 'e', 'o'}
print(set_22_3)  # <- {1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10}
print(set_22_4)  # <- {1, 2, 3, 5, 9, 10}
print(set_22_5)  # <- {}

# --------------------------------------------------------------------------
# Lesson 23 ----- Словари -----

dict_23_1 = {}  # <- ключ: значение
dict_23_2 = {'title': 'Sony', 'price': 100}
dict_23_3 = dict(title='iPhone', price=110)
dict_23_4 = dict.fromkeys(['price', 'price2', 'price3'], 50)
dict_23_5 = {i: i + 1 for i in range(1, 10)}

list_ueser = [  # <- Многоуровневый список
    ['bob@gmail.com', 'Bob'],
    ['katy@gmail.com', 'Katy'],
    ['jhon@gmail.com', 'Jhon'],
]

dict_users = dict(list_ueser)

print(list_ueser)  # <- [['bob@gmail.com', 'Bob'], ['katy@gmail.com', 'Katy'], ['jhon@gmail.com', 'Jhon']]
print(dict_users)  # <- {'bob@gmail.com': 'Bob', 'katy@gmail.com': 'Katy', 'jhon@gmail.com': 'Jhon'}

print(f"{dict_23_1} - {type(dict_23_1)}")
print(dict_23_2)  # <- {'title': 'Sony', 'price': '100'}
print(dict_23_3)  # <- {'title': 'iPhone', 'price': '110'}
print(dict_23_4)  # <- {'price': 50, 'price2': 50, 'price3': 50}
print(dict_23_5)  # <- {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

print(dict_23_1['title'])  # <- Sony
print(dict_23_1.get('title'))  # <- Sony
print(dict_23_2['price'])  # <- 110

for key in dict_23_1:  # <- title, price
    print(key, end=" ")

for key in dict_23_1:  # <- title, price
    print(dict_23_1[key], end=" ")  # <- Sony, 100

for key in dict_23_1:
    print(f"{key}: {dict_23_1[key]}", end=" ")  # <- title: Sony, price: 100

# Метод .items возвращает пару ключ - значение
for key, value in dict_23_1.items():
    print(f"{key}: {value}", end=" ")  # <- title: Sony, price: 100

products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 110},
    {'title': 'Samsung', 'price': 90},
]

print(products)  # <- {'title': 'Sony', 'price': 100}, {'title': 'iPhone', 'price': 110},
# {'title': 'Samsung', 'price': 90},

for product in products:
    print(product['title'], [product['price']])

# --------------------------------------------------------------------------
# Lesson 24 ----- Методы словаря -----

dict_24_1 = {'title': 'Sony', 'price': 100}

"""
dict_24_1.clear() - Очищает словарь
dict_24_1.cope() - Возвращает копию словаря
dict_24_1.get(key[, default]) - Возвращает значение ключа, но если его нет, не бросате исключение, а возвращает 
default (по умолчанию None) 
dict_24_1.items() - Возвращает пары (ключ, значение)
dict_24_1.keys() - Возвращает ключи в словаре
dict_24_1.pop(key,[, default])  - удаляет ключ и возвращает значение
dict_24_1.popitem() - Удаляет и возвращает пару(ключ, значение)
dict_24_1.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other
dict_24_1.values() - возвращает значения в словаре
"""

# --------------------------------------------------------------------------
# Lesson 25 ----- Игра угадай число -----

""" Задача 1 - моё решение без random """

numbers = list(range(1, 101))
numbers = map(str, numbers)
numbers = set(numbers)

rand_number = int(numbers.pop())

count = 0

print("-- Было загаданно число от 1 до 100 --")
print("-- Попробуй угадай --")
while True:
    num_user = int(input("Введите число: "))
    count += 1

    print(" ------- ")

    if num_user == rand_number:
        print(f"Поздравляю, ты выиграл! Загадонное число {rand_number}")
        print(f"Колличество попыток: {count}")
        break
    elif num_user < rand_number:
        print("Твоё число меньше загадонного")
    elif num_user > rand_number:
        print("Твоё число больше загадонного")

    print(" ------- ")

""" Задача 1 - решение преподавателя """

x = 75
user_num = 0
cnt = 0

while True:
    user_num = int(input("Я загадал число от 1 до 100 - угадай его: "))
    cnt += 1
    if user_num == x:
        print(f"Ты угадал число за {cnt} попыток")
        print("Спасибо за игру")
        break
    elif user_num > x:
        print("Моё число меньше")
    else:
        print("Моё число больше")

# --------------------------------------------------------------------------
# Lesson 26 ----- Пользовательские функции. Часть 1 -----


def hello(name, word):
    print(f'Hello, {name}. Say {word}')


def get_sum_print(a, b):
    print(a + b)


def get_sum_return(a, b):
    return a + b


hello('Bob', 'Hi')
get_sum_print(10, 20)
print(get_sum_return(40, 30))

# --------------------------------------------------------------------------
# Lesson 27 ----- Пользовательские функции. Часть 2 -----


def set_register(s):
    """ Дз """
    if ' ' in s:
        return s.upper()
    else:
        return s.lower()


s_value = 'Hello World'
print(set_register(s_value))

# -----


def get_sum_2(a, b, c=0, d=1):  # <- a и b - это позиционные аргументы | с и d это именованные аргументы
    return a + b + c + d


""" Позиционные аргументы передаются первыми, потом уже именованные """
print(get_sum_2(1, 2, 3))

# -----


def get_sum_3(*args):
    return sum(args)


def func_1(**kwargs):
    print(**kwargs)


def func_2(a, b, *args, **kwargs):
    print(f"a - {a}")
    print(f"b - {b}")
    print(f"*args - {args}")
    print(f"**kwargs - {kwargs}")


"""
*{название аргумента} - это произвольное количество аргументов, которые преобразуются в картеж
**{название аргумента} - это произвольное количество аргументов, которые преобразуются в словарь

По сути, *args это позиционные аргументы, а **kwargs это именовынные аргументы

"""
func_2(10, 20, 30, 40, 50, x=60, y=70, z=80)
func_1(a=1, b=5, c=20)
print(get_sum_3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# --------------------------------------------------------------------------
# Lesson 28 ----- Пользовательские функции. Часть 3 -----


def get_sum_4(a: int, b: int) -> int:
    """
    Возвращает сумму вргументов a и b.

    :param a: Первый аперант
    :type a: int
    :param b: Второй аперант
    :type b: int
    :return: Return type int
    """
    return a + b


print(get_sum_4(10, 20))

# -----


def func_3():
    global a

    x = 5  # <- Локальная перемнная
    a += 1

    return a, x


y = 5  # <- Глобальная переменная
a = 5  # <- Глобальная переменная
print(func_3())

# -----


def func_4(list_value):
    return [i * 2 for i in list_value]


def func_5(list_value):
    def get_mult(x):
        return int(x) * 2
    return [get_mult(i) for i in list_value]


arr_nums = [1, 2, 3]
print(func_4(arr_nums))
print(func_5(arr_nums))

# --------------------------------------------------------------------------
# Lesson 29 ----- Решение домашнего задания -----

""" ДЗ 1. Моё решение"""


def func_6(array: list):
    if 'odd' in array:
        if array.index('odd') in array:
            return True
        else:
            return False
    else:
        return 'odd отсутствует'


def odd_ball(arr):
    return arr.index('odd') in arr if 'odd' in arr else 'odd отсутсвует'


list_value7 = [1, 3, 5, 7, 'odd', 10, 8, 20, 14, 4]
print(func_6(list_value7))
print(odd_ball(list_value7))

""" ДЗ 2. Моё решение"""


def find_sum_args(*nums):
    return sum([num for num in nums if num % 3 == 0 or num % 5 == 0])


def find_sum_num(num):
    return sum([n for n in range(num + 1) if n % 3 == 0 or n % 5 == 0])


print(f"Сумма: {find_sum_args(10, 3, 6, 2, 4, 5, 15, 20, 21, 22, 23)}")
print(f"Сумма: {find_sum_num(20)}")

""" ДЗ 3. Моё решение"""


def list_name(array):
    new_array = []
    for name in array:
        if len(name) == 4:
            new_array.append(name)

    return new_array


def list_name_gen(array):
    return [name for name in array if len(name) == 4]


names = ['Ryan', 'Kieran', 'Mark', 'Jhon', 'David', 'Paul']
print(f"Новый писок: {list_name(names)}")
print(f"Новый писок: {list_name_gen(names)}")

""" ДЗ 1. Решение преподавателя"""


def odd_ball(arr):
    return arr.index('odd') in arr


""" ДЗ 2. Решение преподавателя"""


def find_sum_1(n):
    res = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


def find_sum_2(n):
    return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0)


""" ДЗ 3. Решение преподавателя"""


def get_names(names):
    return [i for i in names if len(i) == 0]


# --------------------------------------------------------------------------
# Lesson 30 ----- Модули в Python -----

print(os.getcwd())
print(random.randint(1, 100))

list_123 = [1, 2, 3, 4, 5]
print(random.shuffle(list_123))

str_ = 'Hello World'
print(libs.get_len(str_))
print(libs.get_count(str_, 'l'))

test_f = libs.get_count
print(test_f(str_, 'o'))

# --------------------------------------------------------------------------
# Lesson 31 ----- Модули Datetime-----
