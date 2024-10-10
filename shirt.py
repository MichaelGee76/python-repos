import sys
from PIL import Image
import os.path
import filecmp


def main():

    # check if everything is valid
    valid_extensions = (".jpg", ".jpeg", ".png")
    if len(sys.argv) != 3:
        sys.exit("Please provide 2 arguments")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")
    elif not sys.argv[1].lower().endswith(valid_extensions) and not sys.argv[
        2
    ].lower().endswith(valid_extensions):
        sys.exit("File extension does not match")

    argv_extension_one = (
        sys.argv[1].lower().split(".")[-1]
    )  # greift nur auf den letzten teil der liste zu
    argv_extension_two = sys.argv[2].lower().split(".")[-1]

    if argv_extension_one != argv_extension_two:
        sys.exit("Files do not match")
    # program logic

    bg_image = Image.open(sys.argv[1]).convert("RGBA")
    front_image = Image.open(sys.argv[2]).convert("RGBA")

    front_image = front_image.resize(bg_image.size)

    front_image.paste(bg_image, (0, -25), bg_image)
    front_image.save("result.png")


if __name__ == "__main__":
    main()
