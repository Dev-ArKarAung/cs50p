def main():
    x, y = input("Fraction: ").split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    fraction = x / y
    if fraction >= 0.99:
        print("F")
    elif fraction <= 0.01:
        print("E")
    else:
        print(f"{fraction * 100:.0f}%")

if __name__ == "__main__":
    main()