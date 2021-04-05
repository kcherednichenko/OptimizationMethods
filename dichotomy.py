import math


def dichotomy(f, a, b, eps):
    iterations_amount = int(math.log((b - a) / eps) / math.log(2))

    delta = eps / 4

    # for i in range(iterations_amount):
    while abs(b - a) > eps:
        x1, x2 = (a + b) / 2 - delta, (a + b) / 2 + delta
        f_x1, f_x2 = f(x1), f(x2)

        if f_x1 > f_x2:
            a = x1
        else:
            b = x2

        x_min = (a + b) / 2
        f_min = f(x_min)

    return x_min, f_min


def f(x):
    return math.log(x) * math.sin(x) * x ** 2


print(dichotomy(f, 0, 1, 0.000001))
