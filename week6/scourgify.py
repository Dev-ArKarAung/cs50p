import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    with open(sys.argv[1]) as before_file:
        reader = csv.DictReader(before_file)
        with open(sys.argv[2], "w", newline='') as after_file:
            writer = csv.DictWriter(after_file, fieldnames=["last", "first", "house"])
            writer.writeheader()
            for row in reader:
                name = row["name"]
                last, first = name.split(", ")
                house = row["house"]
                writer.writerow({"last": last, "first": first, "house": house})

if __name__ == "__main__":
    main()
            