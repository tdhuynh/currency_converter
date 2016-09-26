
rates = {'USD': 1, 'JPY': 100.31, 'EUR': .89, 'BTC': .0016}

class Money:

    def __init__(self, amount, symbol):
        self.amount = amount
        self.symbol = symbol

    def __add__(self, other):
        other.amount = rates[self.symbol]/rates[other.symbol] * other.amount
        return self.amount + other.amount, self.symbol

    def __mul__(self, other):
        other.amount = rates[self.symbol]/rates[other.symbol] * other.amount
        return self.amount * other.amount, self.symbol

    def __sub__(self, other):
        other.amount = rates[self.symbol]/rates[other.symbol] * other.amount
        return self.amount - other.amount, self.symbol

    def __ge__(self, other):
        other.amount = rates[self.symbol]/rates[other.symbol] * other.amount
        return self.amount >= other.amount

    def __gt__(self, other):
        other.amount = rates[self.symbol]/rates[other.symbol] * other.amount
        return self.amount > other.amount

    def __le__(self, other):
        other.amount = rates[self.symbol]/rates[other.symbol] * other.amount
        return self.amount <= other.amount

    def __lt__(self, other):
        other.amount = rates[self.symbol]/rates[other.symbol] * other.amount
        return self.amount < other.amount

    def __eq__(self, other):
        other.amount = rates[self.symbol]/rates[other.symbol] * other.amount
        return self.amount == other.amount

    def __ne__(self, other):
        other.amount = rates[self.symbol]/rates[other.symbol] * other.amount
        return self.amount != other.amount

money = Money(20, 'USD')
money2 = Money(50, 'EUR')
# money3 = Money(.89,'EUR')
# money4 = Money(100.31, 'JPY')
print(money + money2)
