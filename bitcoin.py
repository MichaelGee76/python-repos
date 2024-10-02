import sys
import requests
import json


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin_float = float(sys.argv[1])
        data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        rate = data["bpi"]["USD"]["rate"].replace(",", "")

        formatted_rate = "{:,.4f}".format(bitcoin_float * float(rate))
        print(f"${formatted_rate}")
    except ValueError:
        sys.exit("Command-line argument is not a number")


if __name__ == "__main__":
    main()
