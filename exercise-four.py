# Exercise 4

NAME: str = ""
GENDER: str = ""

NAME = input("Geben Sie ihren Namen ein: ")
GENDER = input(
    "Geben Sie ihr Geschlecht ein: "
    "(m = männlich, w = weiblich, n = nonbinär)"
)

if GENDER == "w":
    print(f"{NAME} ist eine Frau.")
elif GENDER == "m":
    print(f"{NAME} ist ein Mann.")
elif GENDER == "n":
    print(f"{NAME} will sein Geschlecht nicht festlegen.")
else:
    print(f"{NAME} hat keine Eingabe gemacht.")
