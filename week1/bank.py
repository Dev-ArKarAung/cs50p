name = input("Greeting: ")

match name:
    case greeting if greeting.startswith("Hello"):
        print("$0")
    case greeting if greeting.startswith("H"):
        print("$20")
    case _:
        print("$100")