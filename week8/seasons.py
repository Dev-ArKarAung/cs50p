from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    minutes = (today - birth_date).days * 24 * 60
    words = p.number_to_words(minutes, andword='')
    print(f"{words} minutes")

if __name__ == "__main__":
    main()




