import os.path
import csv
import operator
import keyboard
import threading
from tabulate import tabulate
from termcolor import colored


def show_usr_list():
    if os.path.isfile("usr_list.csv"):
        with open("usr_list.csv", encoding="utf-8") as usr_list:
            reader = csv.reader(usr_list)
            headers = next(reader)
            sorted_list = sorted(reader, key=operator.itemgetter(2))
            print(
                colored(
                    tabulate(sorted_list, headers=headers, tablefmt="grid"), "green"
                )
            )

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
        with open("usr_list.csv", "r+", newline="", encoding="utf-8") as usr_list:
            fieldnames = ["id", "task", "prio", "done"]
            max_id = []
            max_id_value = 0
            reader = csv.DictReader(usr_list)
            for row in reader:
                max_id.append(row["id"])
            max_id_value = int(max(max_id))
            id = max_id_value + 1
            writer = csv.DictWriter(usr_list, fieldnames=fieldnames)
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


def end_programm():
    print("Alle Daten wurden gespeichert. Bis bald.")


def mark_task_as_done():
    show_usr_list()
    id_usr_choice = int(input("Welche Aufgabe willst du als erledigt markieren? Id: "))
    task_found = True
    updated_data = []

    with open("usr_list.csv", newline="", encoding="utf-8") as usr_list:
        reader = csv.DictReader(usr_list)
        for row in reader:
            if int(row["id"]) == id_usr_choice:
                task_found = True
                if row["done"] == "True":
                    print(
                        colored(
                            f"\nDie Aufgabe mit der Id {id_usr_choice} wurde bereits als erledigt markiert\n",
                            "red",
                        )
                    )
                    return
                else:
                    row["done"] = "True"

            updated_data.append(row)
            if not task_found:
                print(colored("\nId nicht gefunden, wähle eine andere Aufgabe\n"))
                return
    with open("usr_list.csv", "w", newline="", encoding="utf-8") as usr_list:
        fieldnames = ["id", "task", "prio", "done"]
        writer = csv.DictWriter(usr_list, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_data)
    print(
        colored(
            f"\nDie Aufgabe mit Id '{id_usr_choice}' wurde als erledigt markiert\n",
            "green",
        )
    )
