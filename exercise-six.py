number_one: float = float(0)
number_two: float = float(0)
operator: str = ""

number_one = float(input("Geben Sie die erste Nummer ein: "))
number_two = float(input("Geben Sie die zweite Nummer ein: "))
operator = str(input("Geben Sie das Operationszeichen ein (+, -, *, /): "))

if operator == "":
    print("Sie haben kein Operationszeichen angegeben...")
elif operator == "+":
    print(number_one + number_two)
elif operator == "-":
    print(number_one - number_two)
elif operator == "*":
    print(number_one * number_two)
elif operator == "/":
    if number_two == 0:
        print(f"Division durch {number_two} nicht erlaubt.")
    else:
        print(number_one / number_two)
