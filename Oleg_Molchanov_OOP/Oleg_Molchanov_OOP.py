# ------------------------------ 00 ООП Введение (проблемы процедурного программирования) ------------------------------
# Теоретическая информация
# ------------------------------ 01 ООП Объекты и классы ------------------------------
from datetime import datetime
import pytz


class Person:  # <- Созданный класс
    name = 'Ivan'  # <- Атрибут


human = Person()  # <- Экземпляр класса или объект

print(Person.__name__)  # <- Имя класса
print(dir(Person))  # <- Доступные атрибуты
print(Person.__class__)  # <- Класс класса
print(human.__class__)  # <- Класс к которому относится этот экземпляр
print(human.__class__.__name__)

new_human = type(human)()  # <- Создание нового экземляра класса

# ------------------------------ 02 ООП Атрибуты класса и функции ------------------------------


class Person2:
    name = 'Artem'  # <- Атрибут или же поле

    def method_hello(self):  # <- Метод класса
        print("Hello")


print(Person2.__dict__)  # <- Пространство имён классов и экземпляров
print(Person.name)  # <- Обращение к переменной класса
Person2.age = 35  # <- Создание переменной
print(Person2.age)  # <- Обращение к переменной класса
getattr(Person2, 'name')  # <- getatter используется для чтения значений
setattr(Person2, 'dob', '123')  # <- setatter позваляет создавать новые атрибуты или измнять существующие
delattr(Person2, 'dob')  # <- delatter позваляет удалять атрибут

Person2().method_hello()  # <- Вызов метода класса

# ------------------------------ 03 ООП Классы как callble-объекты, экземляры ------------------------------
# Теоретическая информация
# ------------------------------ 04 ООП Функции классов и методы экземляров ------------------------------


class Person3:
    def hello(self):  # <- self это ссылка на экземпляр класса | Эта функция станет методом, когда будет создан объект
        print('Hello')


p = Person3()
print(p.hello)  # <- Метод экземляра класса
print(Person3().hello())  # Hello

# ------------------------------ 05 ООП Инициализация экземпляров, __init__ метод ------------------------------


class Person4:
    def __init__(self, name):  # <- Конструктор
        self.name = name  # <- инициализация поля

    def display(self):
        print(self.name)


p = Person4('Ivan')
p.name = 'Ivan'  # <- тоже самое что и self.name = 'Ivan'

# ------------------------------ 06 ООП Статические методы и @staticmethod ------------------------------


class Person5:
    def hello(self):
        print("Hello")

    @staticmethod
    def goodbye():  # <- Статический метод
        print("Goodbye")


p = Person5()
p.goodbye()

# -------------------------- 07 ООП Инкапсуляция, приватные атрибуты и публичный интерфейс --------------------------


class Person6:
    def __init__(self, name, surname):
        self._name = name  # <- Приватное значение
        self._surname = surname  # <- Приватное значение
        self.name = f'{self._name} {self._surname}'


p = Person6("Olegh", "Molchanov")
print(p.name)

# -------------------------- 08 ООП Пример 1 --------------------------
# -------------------------- 09 ООП Name mangling --------------------------


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])

    def withdrawn(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f"You spent {amount} units")
            self.show_balance()
            self._history.append([-amount, self._get_current_time()])
        else:
            print("Not enough money")
            self.show_balance()

    def show_balance(self):
        print(f"Balance: {self.__balance}")

    def show_histore(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposit'
            else:
                transaction = 'withdrawn'
            print(f"{amount} {transaction} on {date.astimezone()}")


a = Account('artem', 0)
a.deposit(400)
a.deposit(50)
a.withdrawn(250)
a.show_histore()

# -------------------------- 11 ООП Свойства @property, геттеры и сеттеры (getter, setter) --------------------------

name = 'Ivan'


class Person7:
    name = 'Dima'  # Локальная область класса

    def print_name(self):  # <- Метод print_name не видит переменную name = 'Dima'
        print(name)  # <- Будет выводиться Ivan

    @classmethod  # <- Декоратор делает метод классовым
    def test_name(cls):
        cls.name = name  # Теперь поле name можно будет изменить


p = Person7()
p.print_name()  # <- Локальная область экземляра


class Person8:
    def __init__(self, name):
        self.name = name

    # Первый способ сделать подобие __init__
    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()
        return cls(name=name)

    # Второй способ сделать подобие __init__
    @classmethod
    def from_object(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name=name)
        return cls

# -------------------------- 11 ООП Свойства @property, геттеры и сеттеры (getter, setter) --------------------------


class Person9:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print("From set_name()")
        self._name = value

    # name = property(fget=get_name, fset=set_name)  # <- переменная name теперь атрибут класса
    name = property()
    name = name.getter(get_name)
    name = name.setter(set_name)


class Person10:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # name = property(name)

# -------------------------- 12 ООП Свойства только для чтения и вычисляемые свойства --------------------------

