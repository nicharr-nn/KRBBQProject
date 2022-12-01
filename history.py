class History:
    def __init__(self, no, menu, quantity, price):
        self.no = no
        self.menu = menu
        self.quantity = quantity
        self.price = price

    @property
    def no(self):
        return self._no

    @no.setter
    def no(self, no):
        self._no = no

    @property
    def menu(self):
        return self._menu

    @menu.setter
    def menu(self, menu):
        self._menu = menu

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price





