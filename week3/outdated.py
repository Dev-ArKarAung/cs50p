months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ")
        result = convert(date)
        if result is not None:
            print(result)
            break

def convert(date):
    if "/" in date:
        parts = date.split("/")
        if len(parts) == 3:
            month, day, year = parts
            return validate(month, day, year)
    elif "," in date:
        parts = date.split(",")
        if len(parts) == 2:
            month_day, year = parts
            month_day_parts = month_day.strip().split(" ")
            if len(month_day_parts) == 2:
                month_name, day = month_day_parts
                month = months.index(month_name) + 1
                return validate(month, day, year.strip())

        pass
    return None

def validate(month, day, year):
    try: 
        month = int(month)
        day = int(day)
        year = int(year)
        if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
            return f"{month:02}-{day:02}-{year}"
    except ValueError:
        pass
    return None


if __name__ == "__main__":
    main()
    