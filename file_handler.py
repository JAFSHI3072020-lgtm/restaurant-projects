import os

MENU_FILE = "menu.txt"
ORDER_FILE = "orders.txt"


def load_menu():
    menu = []
    if not os.path.exists(MENU_FILE):
        return menu

    with open(MENU_FILE, "r") as file:
        for line in file:
            fid, name, price = line.strip().split(",")
            menu.append({
                "id": int(fid),
                "name": name,
                "price": float(price)
            })
    return menu


def save_menu(menu):
    with open(MENU_FILE, "w") as file:
        for item in menu:
            file.write(f"{item['id']},{item['name']},{item['price']}\n")


def save_order(order_items, total):
    with open(ORDER_FILE, "a") as file:
        file.write("Order:\n")
        for item in order_items:
            file.write(f"{item['name']} - {item['price']}\n")
        file.write(f"Total: {total}\n\n")
