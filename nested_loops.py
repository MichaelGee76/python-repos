def is_valid(s):
    # In range of min 2 and max 6
    if len(s) not in range(2, 7):
        print(f"Ungültig: Länge {len(s)} ist nicht zwischen 2 und 6")
        return False

    # Check if only numbers or letters
    if not s.isalnum():
        print(f"Ungültig: '{s}' enthält ungültige Zeichen")
        return False

    # Check if first two characters are alphabetic
    if not s[0:2].isalpha():
        print(f"Ungültig: '{s[:2]}' sind nicht beide Buchstaben")
        return False

    # Print to track when we find a digit and check conditions
    for i in range(len(s)):
        if s[i].isdigit():
            print(f"Gefundene Zahl: {s[i]} an Position {i}")
            if s[i] == "0":
                print(f"Ungültig: Erste Zahl ist 0")
                return False

            # Check if any letter comes after the first number
            for j in range(i, len(s)):
                print(f"Überprüfe Zeichen '{s[j]}' an Position {j} nach der Zahl")
                if s[j].isalpha():
                    print(f"Ungültig: Buchstabe '{s[j]}' nach Zahl gefunden")
                    return False
            break  # Sobald die erste Zahl gefunden ist, beenden wir die Schleife

    # If all conditions passed
    print(f"'{s}' ist gültig!")
    return True


# Testen
plate = "ABC12A"
is_valid(plate)
