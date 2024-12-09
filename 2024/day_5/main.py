import functools

file = open(0)

rules = []
for line in file:
    if line.isspace():
        break
    rules.append(list(map(int, line.split("|"))))

cache = {}

for x, y in rules:
    cache[(x, y)] = -1
    cache[(y, x)] = 1


def is_ordered(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache and cache[key] == 1:
                return False
    return True


def cmp(x, y):
    return cache.get((x, y), 0)


total = 0
for line in file:
    page = list(map(int, line.split(",")))

    if is_ordered(page):
        continue
        # total += page[len(page) // 2]
    page.sort(key=functools.cmp_to_key(cmp))
    total += page[len(page) // 2]

print(total)
