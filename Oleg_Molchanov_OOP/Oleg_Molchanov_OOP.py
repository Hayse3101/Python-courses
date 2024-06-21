# ------------------------------ 00 ООП Введение (проблемы процедурного программирования) ------------------------------
# Теоретическая информация
# ------------------------------ 01 ООП Объекты и классы ------------------------------
from datetime import datetime
from time import time
from random import choice
import weakref
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


class Person11:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None

    @property
    def surname(self):
        return self.surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None

    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = f'{self._name} {self._surname}'
        return self._full_name


p = Person11('Ivan', 'Ivanoff')

# ----------------------- 13 ООП Наследование, перегрузка методов и расширение функциональности -----------------------


class Person12:  # <- Класс родитель
    age = 0

    def hello(self):
        print("Hello Person")


class Student(Person12):  # <- Наследование класса Person12
    def hello(self):  # <- Перегрузка метода
        print("Hello Student")

    def goodbye(self):  # <- Расширение класса
        print("Goodbye Student")


s = Student()  # <- Экземпляр студента

# ----------


class IntelCpu:
    cpu_socket = 1151
    name = 'Intel'


class I7(IntelCpu):  # <- Подкласс класса IntelCpu
    pass


class I5(IntelCpu):  # <- Подкласс класса IntelCpu
    pass


i5, i7 = I5(), I7()
isinstance(i5, IntelCpu)  # <- True
issubclass(I7, IntelCpu)  # <- True

# -------------------------- 14 ООП Множественное наследование, mro, миксины --------------------------


class Person13:
    def hello(self):
        print("Hello Person")


class Student1(Person13):
    def hello(self):
        print("Hello Student1")


class Prof(Person13):
    def hello(self):
        print("Hello Prof")


class Someone(Student1, Prof):  # <- Множественное наследование
    pass


s_class = Someone()
s_class.hello()  # <- "Hello Student1"

# ----------


class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set')
        print(f'I like {self.food}')


class Person14:
    def hello(self):
        print("Hello Person")


class Student(FoodMixin, Person14):
    food = 'Pizza'

    def hello(self):
        print("Hello Student")


s_class = Student()

# --------------------------  15 ООП Полиморфизм, перегрузка операторов --------------------------


class Person15:
    age = 1

    def __add__(self, value):
        self.age += 1
        return self.age


p_person = Person15()
p_person + 123  # <- 2
p_person + 113  # <- 3

# ----------


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj):
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        raise TypeError('Wrong object')

    def __eq__(self, room_obj):
        if isinstance(room_obj, Room):
            if self.area == room_obj.area:
                return True
            return False


r1 = Room(3, 5)
r2 = Room(4, 7)

# -------------------------- 16 ООП Хэшируемые объекты и равенство --------------------------


class Person16:
    def __init__(self, name_value):
        self._name = name_value

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, person_obj):
        return isinstance(person_obj, Person16) and self.name == person_obj.name


p_person1 = Person16('Ivan')
p_person2 = Person16('Ivan')
print(p_person1 == p_person2)  # <- True
p_person3 = Person16('Oleg')
print(p_person1 == p_person3)  # <- False
d = {p_person1: "Ivanoff Ivan"}
d.get(p_person1)  # <- "Ivanoff Ivan"

# -------------------------- 17 ООП super() и делегирование родителям --------------------------
# -------------------------- 18 ООП Дескрипторы. Non-data дескрипторы --------------------------


class Person17:
    def __init__(self, name_value):
        self.name_value = name


class Student2(Person17):
    def __init__(self, name_value, surname):
        super().__init__(name)
        self.surname = surname


s_student = Student2('Ivan', 'Ivanoff')

# -------------------------- 18 ООП Дескрипторы. Non-data дескрипторы --------------------------


class StringD:
    def __init__(self, value=None):
        if value:
            self.set(value)

    def set(self, value):
        self._value = value

    def get(self):
        return self._value


class Person18:
    def __init__(self, name, surname):
        self.name = StringD(name)
        self.surname = StringD(surname)


p_person4 = Person18('Ivan', 'Ivanoff')

# ----------


class Epoch:
    def __get__(self, intance, owner_class):
        return int(time())


class MyTime:
    epoch = Epoch()


my_time = MyTime()

# ----------

# class Game:
#     @property
#     def rock_paper_scissors(self):
#         return choice(['Rock', 'Paper', 'Scissors'])
#
#     @property
#     def flip(self):
#         return choice(['Heads', 'Tails'])
#
#     @property
#     def dice(self):
#         return choice(range(1, 7))

# game = Game()


class Dice:
    @property
    def number(self):
        return choice(range(1, 7))


class Choice:  # <- Non-date дескриптор
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, obj, owner):
        return choice(self._choice)


class Game:
    dice = Choice(1, 2, 3, 4, 5, 6)
    flip = Choice('Heads', 'Tails')
    rock_paper_scissors = Choice('Rock', 'Paper', 'Scissors')


dice = Dice()
game = Game()

# -------------------------- 19 ООП Дескрипторы данных --------------------------


class Epoch2:
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return int(time())

    def __set__(self, instance, value):
        pass


class MyTime2:
    epoch = Epoch2()


my_time1 = MyTime2()

# ----------


class IntDescriptor:
    def __init__(self):
        self._values = {}

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self._values.get(instance)


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()


v1_vector = Vector()
v2_vector = Vector()
v3_vector = Vector()

# ------------------ 20 ООП Слабые ссылки weakref и проблема хранения данных в экземпляре дескриптора ------------------


# class Person20:
#     def __init__(self, name_value):
#         self.name_value = name
#
#     def __eq__(self, obj):
#         return isinstance(obj, Person20) and self.name_value == obj.name_value
#
#     def __hash__(self):
#         return hash(self.name_value)
#
#
# p20 = Person20('Ivan')


class IntDescriptor2:
    def __init__(self):
        self._values = weakref.WeakKeyDictionary()

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self._values.get(instance)


class Vector2:
    x = IntDescriptor2()
    y = IntDescriptor2()


v1_vector2 = Vector2()
v2_vector2 = Vector2()
v3_vector2 = Vector2()

# ------------------ 21 ООП Метод __set_name__ и хранение данных в экземпляре класса-владельца ------------------


class ValidString:
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.property_name} must be a String, but{type(value).__name__}")
        # key = '_' + self.property_name
        # setattr(instance, key, value)
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # key = '_' + self.property_name
        # return getattr(instance, key, None)
        return instance.__dit__.get(self.property_name, None)


class Person21:
    name = ValidString()
    surname = ValidString()


p21_Person = Person21()
