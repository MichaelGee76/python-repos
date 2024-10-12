import csv
import operator
import os.path
import keyboard
import threading
from tabulate import tabulate
from termcolor import colored, COLORS


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


def show_usr_list():
    if os.path.isfile("usr_list.csv"):
        with open("usr_list.csv", encoding="utf-8") as usr_list:
            reader = csv.reader(usr_list)
            headers = next(reader)
            sorted_list = sorted(reader, key=operator.itemgetter(2))
            print(tabulate(sorted_list, headers=headers, tablefmt="grid"))

    else:
        print(
            colored(
                "Keine Liste zum anzeigen gefunden. Lege zuerst eine Aufgabe an", "red"
            )
        )


def delete_list():
    are_you_sure = (
        input("Möchtest du die Liste wirklich löschen? Schreibe 'ja' oder 'nein'\n")
        .strip()
        .lower()
    )
    if are_you_sure.startswith("j"):
        if os.path.isfile("usr_list.csv"):
            os.remove("usr_list.csv")
            print("Liste gelöscht")
        else:
            print(colored("Nichts zum löschen gefunden", "red"))


def create_task():

    if os.path.isfile("usr_list.csv"):
        add_to_list = get_usr_tasks()
        write_to_csv(1, add_to_list)

    else:
        add_to_list = get_usr_tasks()
        write_to_csv(0, add_to_list)


def write_to_csv(n, list):
    if n == 0:
        with open("usr_list.csv", "w", newline="", encoding="utf-8") as usr_list:
            fieldnames = ["id", "task", "prio", "done"]
            writer = csv.DictWriter(usr_list, fieldnames=fieldnames)
            writer.writeheader()
            id = 1
            for task_dict in list:
                for task, prio in task_dict.items():
                    writer.writerow(
                        {"id": id, "task": task, "prio": prio, "done": False}
                    )
                    id += 1
    if n == 1:
        with open("usr_list.csv", "a", newline="", encoding="utf-8") as usr_list:
            fieldnames = ["id", "task", "prio", "done"]
            writer = csv.DictWriter(usr_list, fieldnames=fieldnames)
            id = 1
            for task_dict in list:
                for task, prio in task_dict.items():
                    writer.writerow(
                        {"id": id, "task": task, "prio": prio, "done": False}
                    )
                    id += 1


def get_usr_tasks():
    def check_for_esc():
        while True:
            if keyboard.is_pressed("esc"):
                break

    esc_thread = threading.Thread(target=check_for_esc)
    esc_thread.start()

    usr_task_list = []
    while True:
        if not esc_thread.is_alive():
            break

        usr_task = input(
            "Was möchtest du machen? Zum Beenden 'ESC' + 'ENTER' drücken\nAufgabe: "
        ).strip()
        if usr_task == "":
            continue

        while True:
            try:
                usr_prio = int(
                    input(
                        "Welche Priorität soll die Aufgabe haben? 1: Hoch 2: Mittel 3: Niedrig\nPriorität: "
                    )
                )

                if usr_prio not in range(1, 4):
                    print("Ungültige Eingabe. Wähle 1, 2 oder 3.")
                    continue
                print(colored("Aufgabe erfolgreich erstellt", "green"))
                break

            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
                continue

        usr_task_list.append({usr_task: usr_prio})

    return usr_task_list


if __name__ == "__main__":
    main()
