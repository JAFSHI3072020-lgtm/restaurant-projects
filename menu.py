def add_food(menu, food):
    for item in menu:
        if item["id"] == food["id"]:
            return False
    menu.append(food)
    return True


def remove_food(menu, food_id):
    for item in menu:
        if item["id"] == food_id:
            menu.remove(item)
            return True
    return False


def search_food(menu, term):
    return [item for item in menu if term.lower() in item["name"].lower()]
