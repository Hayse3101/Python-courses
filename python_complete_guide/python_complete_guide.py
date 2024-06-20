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

