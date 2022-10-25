number_one: float = float(0)
number_two: float = float(0)

number_one = float(input("Geben Sie die erste Nummer ein: "))
number_two = float(input("Geben Sie die zweite Nummer ein: "))

if (number_one % number_two == 0):
    print(f"{number_one} ist ohne Rest durch {number_two} teilbar.")
else:
    print(f"{number_one} ist nicht ohne Rest durch {number_two} teilbar.")
