menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    total = 0
    while True:
        try:
            item = input("Item: ")
            price = get_price(item)
            if price is not None:
                total += price
        except EOFError:
            print()
            print(f"Total: ${total:.2f}")
            break

def get_price(item):
    return menu.get(item.title())


if __name__ == "__main__":
    main()