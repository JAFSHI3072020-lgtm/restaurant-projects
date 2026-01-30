def get_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Please enter a valid number.")


def get_price(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid price.")
