def main():
    time = input("What time is it? ")
    print(convert(time))


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    t = hours + minutes / 60

    if 7.0 <= t <= 8.0:
        return "breakfast time"
    elif 12.0 <= t <= 13.0:
        return "lunch time"
    elif 18.0 <= t <= 19.0:
        return "dinner time"

    
if __name__ == "__main__":
    main()