input = [x.split() for x in open(0).readlines()]

v = [
    "5 of a kind",
    "4 of a kind",
    "full house",
    "3 of a kind",
    "two pair",
    "one pair",
    "high card",
]

vd = [
    "A",
    "K",
    "Q",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "J",
]


def check_hand(hand):
    d = {}
    for i in hand:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        v = list(d.items())
        if i == "J":
            v = sorted(v, key=lambda x: (x[1], vd[::-1].index(x[0])), reverse=True)
            if v[0][0] != "J":
                d[v[0][0]] = d[v[0][0]] + d["J"]
            else:
                if len(v) > 1:
                    d[v[1][0]] = d[v[1][0]] + d["J"]
    for i in d:
        v = list(d.values())
        if 5 in v:
            return "5 of a kind"
        if 4 in v:
            return "4 of a kind"
        if 3 in v:
            if 2 in v:
                return "full house"
            return "3 of a kind"
        if v.count(2) == 2:
            return "two pair"
        if v.count(2) == 1:
            return "one pair"
    return "high card"


a = []
for h, s in input:
    a.append((check_hand(h), h, s))

a = sorted(
    a,
    key=lambda x: (v.index(x[0]), *(vd.index(x[1][i]) for i in range(5))),
    reverse=True,
)

ans = 0
for i, x in enumerate(a):
    ans += int(x[-1]) * (i + 1)

print(ans)
