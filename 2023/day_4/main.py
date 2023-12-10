# lines = open(0).read().strip().splitlines()
# total = 0
# for r, line in enumerate(lines):
#     nums = line.split(": ")[1]
#     winning = nums.split(" | ")[0].split()
#     my_nums = nums.split(" | ")[1].split()
#     won = [n for n in my_nums if n in winning]
#
#
# print(total)

m = {}

for i, x in enumerate(open(0)):
    if i not in m:
        m[i] = 1

    x = x.split(":")[1].strip()
    a, b = [list(map(int, k.split())) for k in x.split(" | ")]
    j = sum(q in a for q in b)

    for n in range(i + 1, i + j + 1):
        m[n] = m.get(n, 1) + m[i]

print(sum(m.values()))
