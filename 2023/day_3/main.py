grid = open(0).read().splitlines()
cs = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        for dr in range(r - 1, r + 2):
            for dc in range(c - 1, c + 2):
                if (
                    dr < 0
                    or dr >= len(grid)
                    or dc < 0
                    or dc >= len(grid[dr])
                    or not grid[dr][dc].isdigit()
                ):
                    continue
                while dc > 0 and grid[dr][dc - 1].isdigit():
                    dc -= 1
                cs.add((dr, dc))

ns = []

for r, c in cs:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    ns.append(int(s))

print(sum(ns))

grid = open(0).read().splitlines()
total = 0

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != "*":
            continue

        cs = set()

        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if (
                    cr < 0
                    or cr >= len(grid)
                    or cc < 0
                    or cc >= len(grid[cr])
                    or not grid[cr][cc].isdigit()
                ):
                    continue
                while cc > 0 and grid[cr][cc - 1].isdigit():
                    cc -= 1
                cs.add((cr, cc))

        if len(cs) != 2:
            continue

        ns = []

        for cr, cc in cs:
            s = ""
            while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                s += grid[cr][cc]
                cc += 1
            ns.append(int(s))

        total += ns[0] * ns[1]

print(total)
