import sys
import pyfiglet
from pyfiglet import Figlet
import random


def main():
    usr_text = input("Input: ").strip()
    font_list = pyfiglet.FigletFont.getFonts()
    # if no argument provided ...
    if len(sys.argv) == 1:
        f = Figlet(font=font_list[random.randint(0, len(font_list) - 1)])
        print(f"Output: {f.renderText(usr_text)}")

    # if 2 arguments provided ...
    if len(sys.argv) == 3:
        print("2 arguments provided")
        # check if 1 argument doesn't start with '-f' or '--font'
        if not (sys.argv[1].startswith("-f") or sys.argv[1].startswith("--font")):
            sys.exit("Input invalid")
        if sys.argv[2] not in font_list:
            sys.exit("Font not available")

        else:
            f = Figlet(font=sys.argv[2])
            print(f"Output: {f.renderText(usr_text)}")

    # if more than 2 arguments provided... exit
    if len(sys.argv) > 3:
        sys.exit("Too many arguments.")


if __name__ == "__main__":
    main()
