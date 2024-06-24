# --------------------------------------------------------------------------
# Lesson 37 ----- Конструктор класса -----


class Person:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f'Hello, my names if {self.name}')


# --------------------------------------------------------------------------
# Lesson 38 ----- Инкапсуляция -----


class Person_two:
    def __init__(self, name):
        self.name = name
        self._age = 20
        self.__id = 100200

    def print_info(self):
        print(f'Name: {self.name}, Age: {self._age}')

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_value):
        error = Exception('Число должно быть 6 значным')

        if len(str(new_value)) == 6:
            self.__id = new_value
        else:
            raise error


# --------------------------------------------------------------------------
# Lesson 40 ----- Наследование -----


class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self._mail = None
        self.__id = 100001

    def print_user_info(self):
        print(f'Name: {self.name}, Mail: {self._mail}, Id: {self.__id}')

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_value):
        error = Exception('Число должно быть 6 значным')

        if len(str(new_value)) == 6:
            self.__id = new_value
        else:
            raise error


class Employee(User):
    company = 'Google'

    def more_info(self):
        print(f'{self.name} works in {self.company}')

# --------------------------------------------------------------------------
# Lesson 41 ----- Полиморфизм -----
