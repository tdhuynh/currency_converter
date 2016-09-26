
rates = {'USD': 1, 'JPY': 100.31, 'EUR': .89, 'BTC': .0016}


def conversion_formula(self, other):
    other.amount = rates[self.symbol]/rates[other.symbol] * other.amount
    return other.amount


class Money:

    def __init__(self, amount, symbol):
        self.amount = amount
        self.symbol = symbol

    def __add__(self, other):
        conversion_formula(self, other)
        return Money(self.amount + other.amount, self.symbol)

    def __mul__(self, other):
        conversion_formula(self, other)
        return Money(self.amount * other.amount, self.symbol)

    def __sub__(self, other):
        conversion_formula(self, other)
        return Money(self.amount - other.amount, self.symbol)

    def __ge__(self, other):
        conversion_formula(self, other)
        return self.amount >= other.amount

    def __gt__(self, other):
        conversion_formula(self, other)
        return self.amount > other.amount

    def __le__(self, other):
        conversion_formula(self, other)
        return self.amount <= other.amount

    def __lt__(self, other):
        conversion_formula(self, other)
        return self.amount < other.amount

    def __eq__(self, other):
        conversion_formula(self, other)
        return self.amount == other.amount

    def __ne__(self, other):
        conversion_formula(self, other)
        return self.amount != other.amount

    def __str__(self):
        return "{} {}".format(self.amount, self.symbol)


sum_all =   Money(.0016, 'BTC') + Money(100.31, 'JPY') + Money(.89, 'EUR') + Money(1, 'USD')
print(sum_all)
