# t = 0
#
# for i, x in enumerate(open(0)):
#     gs = x.strip().split(": ")[1].split("; ")
#     for g in gs:
#         m = {"red": 0, "green": 0, "blue": 0}
#         for e in g.split(", "):
#             a, b = e.split()
#             m[b] = int(a)
#         if m["red"] > 12 or m["green"] > 13 or m["blue"] > 14:
#             break
#     else:
#         t += i + 1
#
# print(t)

t = 0

for i, x in enumerate(open(0)):
    gs = x.strip().split(": ")[1].split("; ")
    tm = {"red": 0, "green": 0, "blue": 0}
    for g in gs:
        m = {"red": 0, "green": 0, "blue": 0}
        for e in g.split(", "):
            a, b = e.split()
            m[b] = int(a)
        for k in tm:
            tm[k] = max(tm[k], m[k])
    t += tm["red"] * tm["green"] * tm["blue"]

print(t)
