import math


def nth_fibonacci_number(n):
    return int((math.pow((1.0 + math.sqrt(5)) / 2, n) - math.pow((1.0 - math.sqrt(5)) / 2, n)) / math.sqrt(5))


def fibonacci(f, a, b, eps):
    count = 0
    calculations_cnt = 0
    list = []

    while (b - a) >= (eps * nth_fibonacci_number(count + 2)):
        count += 1

    nth_fib_num = nth_fibonacci_number(count)
    first_num = nth_fibonacci_number(count + 1)
    second_num = nth_fibonacci_number(count + 2)

    x1 = a + nth_fib_num / second_num * (b - a)
    x2 = a + first_num / second_num * (b - a)

    f_x1 = f(x1)
    f_x2 = f(x2)
    calculations_cnt += 2

    list.append((b, a))

    for i in range(2, count):
        if f_x1 > f_x2:
            a = x1
            x1, f_x1 = x2, f_x2
            x2 = a + nth_fibonacci_number(count - i + 2) / nth_fibonacci_number(count - i + 3) * (b - a)
            f_x2 = f(x2)
        else:
            b = x2
            x2, f_x2 = x1, f_x1
            x1 = a + nth_fibonacci_number(count - i + 1) / nth_fibonacci_number(count - i + 3) * (b - a)
            f_x1 = f(x1)

        calculations_cnt += 1
        list.append((b, a))

    x_min = a
    f_min = f(a)
    return x_min, f_min, count - 2, calculations_cnt, list


def f(x):
    return math.log(x) * math.sin(x) * x ** 2


print(fibonacci(f, 0, 1, 0.000001))
