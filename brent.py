import math


def signum(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def parabolic(x1, x2, x3, y1, y2, y3):
    return x2 - 0.5 * (math.pow(x2 - x1, 2) * (y2 - y3) - math.pow(x2 - x3, 2) * (y2 - y1)) / (
                (x2 - x1) * (y2 - y3) - (x2 - x3) * (y2 - y1))


def brent(f, a, b, eps):
    const = (3 - math.sqrt(5)) / 2
    list = []
    count = 0
    v_y = 0
    u = v = z = x = a + const * (b - a)
    f_x = f_v = f_z = f(x)
    v_y += 1
    c = e = b - a
    list.append((b, a))
    while c > eps:
        count += 1
        is_par = False
        temp, e = e, c
        if x != v and x != z and v != z and f_x != f_v and f_x != f_z and f_v != f_z:
            u = parabolic(x, z, v, f_x, f_z, f_v)
            if a + eps <= u <= b - eps and abs(u - x) < temp / 2:
                c = abs(u - x)
                is_par = True
        if not is_par:
            if x < (b - a) / 2:
                u, c = x + const * (b - x), b - x
            else:
                u, c = x - const * (x - a), x - a
            if abs(u - x) < eps:
                u = x + signum(u - x) * eps
        fu = f(u)
        v_y += 1
        if fu <= f_x:
            if u >= x:
                a = x
            else:
                b = x
            v, z, x = z, x, u
            f_v, f_z, f_x = f_z, f_x, fu
        else:
            if u >= x:
                b = u
            else:
                a = u
            if fu <= f_z or z == x:
                v, z, f_v, f_z = z, u, f_z, fu
            elif fu <= f_v or v == x or v == z:
                v, f_v = u, fu
        list.append((b, a))
    return x, count, v_y, list


def f(x):
    return math.log(x, 10) * math.sin(x) * x ** 2


print(brent(f, 2, 5, 0.000001))
