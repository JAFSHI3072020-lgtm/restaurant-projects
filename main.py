from menu import add_food, remove_food, search_food
from order import take_order
from file_handler import load_menu, save_menu, save_order
from utils import get_int, get_price


def show_menu(menu):
    if not menu:
        print("Menu is empty.")
        return

    print("\n--- Restaurant Menu ---")
    for item in menu:
        print(f"{item['id']}. {item['name']} - {item['price']} TK")


def main():
    menu = load_menu()

    while True:
        print("\n===== RESTAURANT MANAGEMENT =====")
        print("1. Add Food Item")
        print("2. View Menu")
        print("3. Search Food")
        print("4. Take Order")
        print("5. Remove Food Item")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fid = get_int("Food ID: ")
            name = input("Food Name: ")
            price = get_price("Price: ")

            food = {"id": fid, "name": name, "price": price}

            if add_food(menu, food):
                save_menu(menu)
                print("Food item added.")
            else:
                print("Food ID already exists.")

        elif choice == "2":
            show_menu(menu)

        elif choice == "3":
            term = input("Enter food name to search: ")
            results = search_food(menu, term)
            for item in results:
                print(item["name"], "-", item["price"])

        elif choice == "4":
            items, total = take_order(menu)
            save_order(items, total)
            print("Total Bill:", total)

        elif choice == "5":
            fid = get_int("Enter food ID to remove: ")
            if remove_food(menu, fid):
                save_menu(menu)
                print("Food removed.")
            else:
                print("Food not found.")

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
