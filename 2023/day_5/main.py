# import re
#
#
# input = open(0).read().strip().split("\n\n")
#
# [[seeds], *maps] = [
#     [[*map(int, s.split())] for s in y.split("\n")]
#     for y in [re.split(r": |:\n", x)[1] for x in input]
# ]
#
#
# def f(arr, cmap):
#     ans = []
#     for n in arr:
#         a = n
#         for m in cmap:
#             if n in range(m[1], m[1] + m[2]):
#                 a = m[0] + n - m[1]
#         ans.append(a)
#     return ans
#
#
# n = 0
# s = []
# for i in range(0, len(seeds), 2):
#     for x in range(seeds[i], seeds[i] + seeds[i + 1]):
#         s.append(x)
# while n < len(maps):
#     s = f(s, maps[n])
#     n += 1
#
# print(min(s))

inputs, *blocks = open(0).read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))
    seeds = new

print(min(seeds)[0])
