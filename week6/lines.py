import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    lines = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                stripped = line.strip()
                if stripped == "" or stripped.startswith("#"):
                    continue
                lines += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(lines)

if __name__ == "__main__":
    main()