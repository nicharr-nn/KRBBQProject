import json
from order import Order
from user import User


class App:
    def __init__(self):
        self.user = None
        self.order = None
        self.history = None

    def update(self, menu, quantity):
        with open('stock.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            for item in data:
                if item['Menu'] == menu:
                    item['Stock'] -= quantity
                    break
            with open('stock.json', 'w') as jf:
                json.dump(data, jf, indent=4)

    def run(self):
        self.user = User()
        self.user.login()
        self.user.ask()
        self.user.check_table()
        self.order = Order()
        self.order.display_menu()
        self.order.choose_menu()
        self.user.get_cart(self.order.cart)
        if self.user.summary() is False:
            print('Quit')
            exit()
        else:
            self.user.total()
            self.user.confirm()
            for item in self.order.cart:
                self.update(item.menu, item.quantity)


if __name__ == '__main__':
    app = App()
    app.run()
