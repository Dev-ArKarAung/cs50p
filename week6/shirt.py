import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(("jpg", "jpeg", "png")):
        sys.exit("Invalid input")
    if not sys.argv[2].endswith(("jpg", "jpeg", "png")):
        sys.exit("Invalid output")   

    try:
        input_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    fitted = ImageOps.fit(input_image, shirt.size)
    fitted.paste(shirt, (0, 0), shirt)
    fitted.save(sys.argv[2])


if __name__ == "__main__":
    main()