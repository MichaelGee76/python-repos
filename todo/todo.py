# import csv
# import operator
# import os.path
# import keyboard
# import threading
# from tabulate import tabulate
# from termcolor import colored, COLORS
from helpers import *


def main():
    is_on = True
    # print(COLORS)
    print("\nWillkommen zu TODO\n")
    while is_on:

        try:
            usr_answer = int(
                input(
                    "Wähle eine Option:\n1. Aufgabe hinzufügen\n2. Liste anzeigen\n3. Aufgabe als erledigt markieren\n4. Liste löschen\n5. Programm beenden\n"
                )
            )
        except ValueError:
            continue
        if usr_answer == 5:
            print("Bis bald")
            break
        if usr_answer == 1:
            create_task()
        if usr_answer == 2:
            show_usr_list()
        if usr_answer == 4:
            delete_list()


if __name__ == "__main__":
    main()
