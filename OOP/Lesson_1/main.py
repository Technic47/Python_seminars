class Purse:
    def __init__(self, currency, name='Unknown'):  # конструктор объекта. запускается при создании объекта
        if currency not in ('RUB', 'EUR'):
            raise ValueError
        self.__money = 0.00  # с __ изменение значения только из класса. Инкапсуляция (защита)
        self.currency = currency
        self.name = name

    def top_up_balance(self, howmuch):
        self.__money = self.__money + howmuch
        return howmuch

    def top_down_balance(self, howmuch):
        if self.__money - howmuch < 0:
            print('Not enough money!')
            raise ValueError('Not enough money!')
        self.__money = self.__money - howmuch
        return howmuch

    def info(self):
        print(self.__money)

    def __del__(self):  # деструктор. Так же работает при завершении программы
        print('Purse deleted')


x = Purse('RUB')
y = Purse('RUB', 'Marta')

x.top_up_balance(100)
y.top_up_balance(x.top_down_balance(70))
x.info()
y.info()
#del(x)
