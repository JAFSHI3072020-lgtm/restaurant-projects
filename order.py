def take_order(menu):
    order_items = []
    total = 0

    while True:
        food_id = input("Enter food ID (or 'done' to finish): ")
        if food_id.lower() == "done":
            break

        for item in menu:
            if str(item["id"]) == food_id:
                order_items.append(item)
                total += item["price"]
                print(f"Added: {item['name']}")
                break
        else:
            print("Food item not found.")

    return order_items, total
