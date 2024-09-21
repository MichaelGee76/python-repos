def main():
    guests = [
        "Michael",
        "Tom",
        "Freddy",
        "Yussuf",
        "Amber",
        "Fredda",
        "Antonio",
        "Silke",
        "Herman",
    ]
    host = "Frank III."
    for guest in guests:
        print(write_letter(guest, host))


def write_letter(receiver, sender):
    return f"""
    ------------------------------
      Dear {receiver},

      I would like to invite you to my party
      at my castle this evening, 7:00pm.

      Best regards,

      {sender}
    ------------------------------

    """


if __name__ == "__main__":
    main()
