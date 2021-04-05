import math


def f(x):
    return math.log(x) * math.sin(x) * x ** 2


def parabolic(f, a, b, eps=0.000001):
    cnt = 0
    x1, x2, x3 = a, (a + b) / 2, b
    y1, y2, y3 = f(x1), f(x2), f(x3)
    while x3 - x1 >= eps:
        cnt += 1
        u = x2 - ((((x2 - x1) ** 2) * (y2 - y3) - ((x2 - x3) ** 2) * (y2 - y1))
                  / (2 * ((x2 - x1) * (y2 - y3) - (x2 - x3) * (y2 - y1))))
        fu = f(u)
        if u < x2:
            u, x2 = x2, u
            y2, fu = fu, y2
        if y2 <= fu:
            x3, y3 = u, fu
        else:
            x1 = x2
            y1 = y2
            x2 = u
            y2 = fu

    x_min, f_min = x1, f(x1)
    return x_min, f_min, cnt


def f(x):
    return math.log(x) * math.sin(x) * x ** 2


print(parabolic(f, 0.5, 1, 0.000001))
