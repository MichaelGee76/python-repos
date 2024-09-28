import requests
import sys
import json


def main():
    data = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
    )
    data_object = data.json()

    for result in data_object["results"]:
        print("Song:", result["trackName"], "Price: $", result["trackPrice"])


if __name__ == "__main__":
    main()
