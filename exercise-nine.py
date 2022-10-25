# Does not work

from math import sqrt


def lin_fun(x_1, y_1, x_2, y_2):
    d_x = x_2 - x_1
    d_y = y_2 - y_1

    d_xy = (d_y / d_x)
    off = (y_1 - x_1) * d_xy

    return [d_xy, off]


p_one_x: float = float(
    input("Geben Sie die X-Koordinate vom ersten Punkt ein: "))
p_one_y: float = float(
    input("Geben Sie die Y-Koordinate vom ersten Punkt ein: "))
p_two_x: float = float(
    input("Geben Sie die X-Koordinate vom zweiten Punkt ein: "))
p_two_y: float = float(
    input("Geben Sie die Y-Koordinate vom zweiten Punkt ein: "))

fun = lin_fun(p_one_x, p_one_y, p_two_x, p_two_y)
print(f"f(x) = {fun[0]} * x + {fun[1]}")
