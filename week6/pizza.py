import csv
from tabulate import tabulate
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    pizzas = []

    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            pizzas.append({"Regular Pizza": row[0], "Small": row[1], "Large": row[2] })

    print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()