def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            break
        except ValueError:
            pass
    print(gauge(percent))

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ValueError
    if x > y:
        raise ValueError
    percentage = (x / y) * 100
    return percentage

def gauge(percentage):
    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{percentage * 1:.0f}%")


if __name__ == "__main__":
    main()