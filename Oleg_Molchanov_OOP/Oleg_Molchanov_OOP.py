# ------------------------------ 00 ООП Введение (проблемы процедурного программирования) ------------------------------
# Теоретическая информация
# ------------------------------ 01 ООП Объекты и классы ------------------------------


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

