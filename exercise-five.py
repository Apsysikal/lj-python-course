name = input("Wie heissen Sie?: ")


def print_row_delimiter():
    print("=" * 40)


print_row_delimiter()

if name == "James Bond":
    print("Hallo James")
    print()
    print("Wir haben einen neuen Hacker in der Ausbildung.")
    print("Er kann schon geheime Nachrichten für dich erstellen lassen.")
    print("Passen Sie auf sich auf.")
    print()
    print("M")
else:
    print("Diese Nachricht ist nicht für Sie.")

print_row_delimiter()
