import json
from history import History


class Order:
    def __init__(self):
        self.cart = []

    def display_cart(self):
        print('-' * 70)
        print(f"{'No':^3} {'Menu':^25} {'Quantity':^15} {'Price':^10}")
        print('-' * 70)
        for item in range(len(self.cart)):
            print(f"{self.cart[item].no:<3} {self.cart[item].menu:<25} {self.cart[item].quantity:^15}"
                  f" {self.cart[item].price:^3} Baht")
        print('-' * 70)

    def display_menu(self):
        with open('stock.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            print('-' * 70)
            print(f"{'No':^3} {'Menu':^25} {'Stock':^15} {'Price':^10}")
            print('-' * 70)
            for item in data:
                print(f"{item['No.']:<3} {item['Menu']:<25} {item['Stock']:^15} {item['Price']:<3} Baht")
            print('-' * 70)

    def check_stock(self, stock, quantity):
        if stock >= quantity:
            return True
        else:
            print('Not enough stock')
            return False

    def choose_menu(self):
        while True:
            choose = input('(show) cart, (add), (remove) menu or enter name to (confirm) order?: ')
            if choose == 'add':
                self.add_list()
            elif choose == 'remove':
                self.remove_list()
            elif choose == 'show':
                self.display_cart()
            elif choose == 'confirm':
                break
            else:
                print('Failed, please try again')

    def add_list(self):
        choose = input('Please input the number of the menu you want to add: ')
        with open('stock.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            for item in data:
                if item['No.'] == choose:
                    print(f"You choose {item['Menu']}")
                    quantity = int(input('Please input the quantity: '))
                    if self.check_stock(item['Stock'], quantity):
                        if self.check_menu_in_cart(choose):
                            for i in self.cart:
                                if i.no == choose:
                                    i.quantity += quantity
                            print(f"Added {quantity} {item['Menu']} to cart")
                        else:
                            print(f"Added {quantity} {item['Menu']} to cart")
                            self.cart.append(History(item['No.'], item['Menu'], quantity, item['Price']))
                    break
            else:
                print('Not found')

    def remove_list(self):
        self.display_cart()
        choose = input('Please input the number of the menu you want to remove: ')
        for item in self.cart:
            if item.no == choose:
                self.cart.remove(item)
                print(f"Removed {item.menu} from cart")
                break
            else:
                print('Not found')
                break

    def check_menu_in_cart(self, choose):
        for item in self.cart:
            if item.no == choose:
                return True
        return False
