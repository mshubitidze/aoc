groups = [x.split() for x in open(0).read().split("\n\n")]

ans = 0
for group in groups:
    if len(group) > 1:
        s = set()
        for p in group:
            for i in p:
                s.add(i)
        for i in list(s):
            if all(i in x for x in group):
                ans += 1
    else:
        ans += len(group[0])

print(ans)
