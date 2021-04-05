import math


def golden_section(f, a, b, eps):
    c = (3 - math.sqrt(5)) / 2

    x1, x2 = a + c * (b - a), b - c * (b - a)
    f_x1, f_x2 = f(x1), f(x2)
    cnt = 2

    while b - a > eps:
        if f_x1 > f_x2:
            a = x1
            x1 = x2
            x2 = b - c * (b - a)

            f_x1 = f_x2
            f_x2 = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + c * (b - a)

            f_x2 = f_x1
            f_x1 = f(x1)

        cnt += 1

    x_min = (x1 + x2) / 2
    f_min = f(x_min)

    return x_min, f_min, cnt


def f(x):
    return math.log(x) * math.sin(x) * x ** 2


print(golden_section(f, 0, 1, 0.000001))
