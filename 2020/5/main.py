passes = open(0).read().split()

def id(s):
    r = s[:7]
    c = s[7:]
    
    rows = list(range(128))
    cols = list(range(8))

    row = []
    col = []
    for i in r:
        if i == "F":
            row = rows[:len(rows)//2]
            rows = row
        else:
            row = rows[len(rows)//2:]
            rows = row

    for i in c:
        if i == "L":
            col = cols[:len(cols)//2]
            cols = col
        else:
            col = cols[len(cols)//2:]
            cols = col

    return [row[0], col[0]]


l = []
for p in passes:
    row, col = id(p)
    r = int(row)
    c = int(col)
    ans = r * 8 + c
    l.append(ans)

print(max(l))

for i in range(64,935):
    if i not in l:
        print(i)
