from math import sqrt


def distance(x_1, y_1, x_2, y_2):
    d_x = abs(x_1 - x_2)
    d_y = abs(y_1 - y_2)
    return sqrt((d_x*d_x) + (d_y * d_y))


p_one_x: float = float(
    input("Geben Sie die X-Koordinate vom ersten Punkt ein: "))
p_one_y: float = float(
    input("Geben Sie die Y-Koordinate vom ersten Punkt ein: "))
p_two_x: float = float(
    input("Geben Sie die X-Koordinate vom zweiten Punkt ein: "))
p_two_y: float = float(
    input("Geben Sie die Y-Koordinate vom zweiten Punkt ein: "))
r: float = abs(float(
    input("Geben Sie die zu vergleichende Distanz ein: ")))
dst = distance(p_one_x, p_one_y, p_two_x, p_two_y)

print(f"Punkt 1: {p_one_x}/{p_one_y}")
print(f"Punkt 2: {p_two_x}/{p_two_y}")
print(f"Distanz: {distance(p_one_x, p_one_y, p_two_x, p_two_y)}")

if dst == r:
    print("Die Distanz zwischen den Punkten ist gleich wie die eingegebene Distanz")
elif dst >= r:
    print("Die Distanz zwischen den Punkten ist grösser wie die eingegebene Distanz")
elif dst <= r:
    print("Die Distanz zwischen den Punkten ist kleiner wie die eingegebene Distanz")
else:
    print("How did you get here?")
