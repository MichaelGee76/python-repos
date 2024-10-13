from helpers import *


def main():
    is_on = True
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
            end_programm()
            break
        if usr_answer == 1:
            create_task()
        if usr_answer == 2:
            show_usr_list()
        if usr_answer == 3:
            mark_task_as_done()
        if usr_answer == 4:
            delete_list()


if __name__ == "__main__":
    main()
