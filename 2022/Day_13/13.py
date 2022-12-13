x = list(map(str.splitlines, open("input.prod").read().strip().split("\n\n")))


def f(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return f([x], y)
    else:
        if type(y) == int:
            return f(x, [y])

    for a, b in zip(x, y):
        v = f(a, b)
        if v:
            return v

    return len(x) - len(y)


t = 0

for i, (a, b) in enumerate(x):
    if f(eval(a), eval(b)) < 0:
        t += i + 1

print(t)

x1 = list(map(eval, open("input.prod").read().split()))

i2 = 1
i6 = 2

for a in x1:
    if f(a, [[2]]) < 0:
        i2 += 1
        i6 += 1
    elif f(a, [[6]]) < 0:
        i6 += 1

print(i2 * i6)
