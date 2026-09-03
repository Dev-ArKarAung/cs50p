def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = greeting.strip().lower()
    match greeting:
        case _ if greeting.startswith("hello"):
            return "$0"
        case _ if greeting.startswith("h"):
            return "$20"
        case _:
            return "$100"


if __name__ == "__main__":
    main()