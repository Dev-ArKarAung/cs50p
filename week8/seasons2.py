# Accidentally built a more complex project so here we are
import datetime as dt
import inflect
p = inflect.engine()

class Date:
    def __init__(self, birth_date, today_date ):
        self.birth_date = birth_date
        self.today_date = today_date

    def __str__(self):
        minutes = (self.today_date - self.birth_date).days * 1440
        words = p.number_to_words(minutes, andword='')
        return f"{words} minutes"

    @classmethod   
    def get(cls):
        today_date = dt.date.today()
        birth_date = dt.date.fromisoformat(input("Date of Birth: "))
        return cls(birth_date, today_date)



def main():
    date = Date.get()
    print(date)


...


if __name__ == "__main__":
    main()