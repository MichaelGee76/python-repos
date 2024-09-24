def main():
    months_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        try:
            usr_answer = input("Date: ").strip()

            if any(month in usr_answer for month in months_list) and "/" in usr_answer:
                continue

            month, day, year = check_separator(usr_answer)
            if month is None or day is None or year is None:
                continue
            if month.capitalize() in months_list:
                if "," not in usr_answer:
                    continue
                index = months_list.index(month.capitalize()) + 1
                day = int(day.replace(",", ""))
                if int(day) > 31:
                    continue
                print(f"{year}-{index:02}-{day:02} ")
                break
            elif int(month) in range(1, 13):
                day = int(day.replace(",", ""))
                if day > 31:
                    continue
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
        except (EOFError, ValueError):
            continue


def check_separator(string):

    if "/" in string:
        parts = string.split("/")
        for part in parts:
            if not part.isdigit():
                return None, None, None
        return parts

    elif " " in string:
        return string.split(" ")
    return None, None, None


if __name__ == "__main__":
    main()
