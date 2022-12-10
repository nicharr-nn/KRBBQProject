# Korean Barbecue Ordering

Program for you to order menu in the restuarant. Through this program, you can order food by letting you fill in the name and table number, you can also add or remove the menu items. After confirming your order, a summary of the list and the balance will appear.

## **4 Classes**
1. User `user.py`
- Ask the user if the user wants to login or not. If the user wants to, ask the user's username and password(read from data.json). If not, user need to input 'guest'.
- After login, ask the user number at which they are seated. There will only be 5 tables at the restaurant. If they were not entered correctly, the program will ask the user to input again.
- Display summary contain the price and total. Also ask if the user wants cancel or confirm.
- Read and write latest order (from order_list.json)
- Show latest ordered if user ask. If user is going to leave, it will clear the history


2. Order `order.py`
- Display the menu(read from stock.json) and cart
- Also can check if the menu is in stock or not, After the customer orders.
- Can also remove menu from the cart


3. History (list of order object) `history.py`
- getter and setter for cart contain No., Menu, Quantity, Price


4. App (Class for runner(main)) `app.py`
- Have 'update' method for deduct the amount of menu in stock (read from stock.json)
- Main

## **Required libraries and tools**
- Python Version 3.10

## **Source files**
- `data.json` : contains username and password
- `stock.json` : contains menu no., name of the menu, and amount of stocks
- `order_list.json` : contains username, table that user sit, and latest ordered(menu no., table that user sit, and amount)
