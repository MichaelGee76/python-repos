import sys
from PIL import Image, ImageOps
import os.path


def main():
    # Check if everything is valid
    valid_extensions = (".jpg", ".jpeg", ".png")
    if len(sys.argv) != 3:
        sys.exit("Please provide 2 arguments")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")
    elif not sys.argv[1].lower().endswith(valid_extensions) or not sys.argv[
        2
    ].lower().endswith(valid_extensions):
        sys.exit("File extension does not match")

    input_extension = sys.argv[1].lower().split(".")[-1]
    output_extension = sys.argv[2].lower().split(".")[-1]

    if input_extension != output_extension:
        sys.exit("Input and output file extensions must match")

    # user input image
    try:
        input_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input file not found")

    # shirt.png open
    try:
        shirt_image = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt image not found")

    # get size of shirt and resize user image to same size like shirt
    size = shirt_image.size
    input_image = ImageOps.fit(input_image, size)

    # shirt on user image
    input_image.paste(shirt_image, (0, 0), shirt_image)

    # save as 2. argument from program call
    input_image.save(sys.argv[2])


if __name__ == "__main__":
    main()
