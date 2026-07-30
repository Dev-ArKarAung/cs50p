name = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

match name:
    case "42" | "forty-two" | "Forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")