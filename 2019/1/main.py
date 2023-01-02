input = [int(x) for x in open(0).read().splitlines()]

total = 0
for i in input:
    while i > 6:
        total += i // 3 - 2
        i = i // 3 - 2

print(total)
