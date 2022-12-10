import json


class User:
    def __init__(self):
        self.__name = None
        self.__password = None
        self.cart = []
        self.table = None

    def login(self):
        while True:
            name = input('Please input your username or "guest": ')
            if name == 'guest':
                print('Welcome guest!')
                self.__name = name
                break
            else:
                with open('data.json', 'r') as jsonFile:
                    data = json.load(jsonFile)
                    if name in data:
                        password = input('Please input your password: ')
                        if password == data[name]:
                            print(f'Welcome {name}!')
                            self.__name = name
                            break
                        else:
                            print('Wrong password, please try again')
                    else:
                        print('Username not found, please try again')

    def check_table(self):
        with open('order_list.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            with open('data.json', 'r') as jf:
                d = json.load(jf)
                for i in range(len(data)):
                    if data[i]['Name'] == self.__name or self.__name == 'guest' or self.__name in d:
                        if data[i]['Table'] == "" or self.__name == 'guest':
                            while True:
                                table = input('Please input the number of the table you want to sit: ')
                                if table in ['1', '2', '3', '4', '5'] \
                                        and table not in [data[i]['Table'] for i in range(len(data))]:
                                    print('Table found!')
                                    print(f'Your table is {table}')
                                    self.table = table
                                    break
                                else:
                                    print('Table not found/available, please try again')
                        else:
                            change = input(f'Your table is {data[i]["Table"]}, do you want to change? (y/n): ')
                            if change == 'y':
                                while True:
                                    table = input('Please input the number of the table you want to sit: ')
                                    if table in ['1', '2', '3', '4', '5'] \
                                            and table not in [data[i]['Table'] for i in range(len(data))]:
                                        print('Table found!')
                                        print(f'Your table is {table}')
                                        self.table = table
                                        break
                                    else:
                                        print('The table is not available, please try again')
                            elif change == 'n':
                                print(f'Your table is {data[i]["Table"]}')
                                self.table = data[i]['Table']
                            else:
                                print('Wrong input, please try again')
                        break

    def ask(self):
        while True:
            if self.__name == 'guest':
                break
            else:
                ask = input('Do you want to order, see the latest ordered,'
                            ' quit or leaving the table? (order/latest/quit/leave): ')
                if ask == 'latest':
                    self.display_history()
                elif ask == 'order':
                    break
                elif ask == 'quit':
                    print('Thank you')
                    exit()
                elif ask == 'leave':
                    print('Thank you for coming')
                    self.leaving()
                    exit()
                else:
                    print('Wrong input, please try again')

    def summary(self):
        if self.cart:
            print('-' * 70)
            print(f"{'No':<3} {'Menu':^25} {'Quantity':^15} {'Price':<10}")
            print('-' * 70)
            for item in range(len(self.cart)):
                print(f"{self.cart[item].no:<3} {self.cart[item].menu:^25} {self.cart[item].quantity:^15}"
                      f" {self.cart[item].price:<3} Baht")
            print('-' * 70)
            return True
        else:
            print('-' * 70)
            print('No order')
            print('-' * 70)
            return False

    def confirm(self):
        while True:
            confirm = input('Do you want to confirm your order? (y/n): ')
            print('-' * 70)
            if confirm == 'y':
                print('Thank you for your order, we will serve your order soon!')
                if self.__name == 'guest':
                    pass
                else:
                    self.data_list()
                break
            elif confirm == 'n':
                print('Order canceled!')
                exit()
            else:
                print('Wrong input, please try again')

    def get_cart(self, cart):
        self.cart = cart

    def total(self):
        total = 0
        for item in self.cart:
            total += item.price
        print(f'Total: {total} Baht')
        if self.__name != 'guest':
            total = total * 0.95
            print(f'Total after discount: {total:.2f} Baht')
        print('-' * 70)

    def display_history(self):
        with open('order_list.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            for i in range(len(data)):
                if data[i]['Name'] == self.__name:
                    print('-' * 70)
                    print("Your latest order is: ")
                    for item in data[i]['Ordered']:
                        print(f"{item['Menu']} {item['Quantity']}")
                    print('-' * 70)
                    break
                else:
                    print('-' * 70)
                    print('You have not ordered yet')
                    print('-' * 70)
                    break

    def data_list(self):
        if self.__name == 'guest':
            pass
        with open('order_list.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            for i in range(len(data)):
                if data[i]['Name'] == self.__name:
                    data[i]['Table'] = self.table
                    data[i]['Ordered'].clear()
                    for item in self.cart:
                        data[i]['Ordered'].append({'No.': item.no, 'Menu': item.menu, 'Quantity': item.quantity})
                    break
            else:
                data.append({'Name': self.__name, 'Ordered': [], 'Table': self.table})
                for item in self.cart:
                    data[-1]['Ordered'].append({'No.': item.no, 'Menu': item.menu, 'Quantity': item.quantity})
            with open('order_list.json', 'w') as jf:
                json.dump(data, jf, indent=4)

    def leaving(self):
        with open('order_list.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            for i in range(len(data)):
                if data[i]['Name'] == self.__name:
                    data[i]['Ordered'].clear()
                    data[i]['Table'] = ""
                    break
            with open('order_list.json', 'w') as jf:
                json.dump(data, jf, indent=4)


