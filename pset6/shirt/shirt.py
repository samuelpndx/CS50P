from PIL import Image, ImageOps
import sys
import os


def main():
    formats = [".jpg", ".jpeg", ".png"]
    check_n_arguments(sys.argv, 3)
    check_formats(sys.argv, formats)
    overlay_img(sys.argv)


def overlay_img(arguments):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(arguments[1]) as input:
            input = ImageOps.fit(input, shirt.size)
            input.paste(shirt, mask = shirt)
            input.save(arguments[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_formats(arguments, formats):
    inp = os.path.splitext(arguments[1])
    out = os.path.splitext(arguments[2])
    if inp[1].lower() not in formats or out[1].lower() not in formats:
        sys.exit("Invalid output")
    elif inp[1].lower() != out[1].lower():
        sys.exit("Input and output have different extensions")
    return None


def check_n_arguments(arguments, n):
    if len(arguments) < n:
        sys.exit("Too few command-line arguments")
    elif len(arguments) > n:
        sys.exit("Too many command-line arguments")
    return None


if __name__ == "__main__":
    main()