import requests
import sys
import json


def main():
    if len(sys.argv) != 2:
        sys.exit()
    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=100&term=" + sys.argv[1]
    )
    # print(json.dumps(response.json(), indent=2))

    data = response.json()

    for result in data["results"]:
        print(result["trackName"])


if __name__ == "__main__":
    main()
