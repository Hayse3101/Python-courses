def make_title(func):
    def warpped():
        return func().capitalize().replace(',', '')
    return warpped


@make_title
def hi():
    return 'hello, world!'


print(hi())
