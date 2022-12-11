grid = [list(map(int, line)) for line in open("input.prod").read().splitlines()]

# Problem #1
t = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        k = grid[r][c]
        if (
            all(grid[r][x] < k for x in range(c))
            or all(grid[r][x] < k for x in range(c + 1, len(grid[r])))
            or all(grid[x][c] < k for x in range(r))
            or all(grid[x][c] < k for x in range(r + 1, len(grid)))
        ):
            t += 1

print(t)

# Problem #2
t = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        k = grid[r][c]
        L = R = U = D = 0
        for x in range(c - 1, -1, -1):
            L += 1
            if grid[r][x] >= k:
                break
        for x in range(c + 1, len(grid[r])):
            R += 1
            if grid[r][x] >= k:
                break
        for x in range(r - 1, -1, -1):
            U += 1
            if grid[x][c] >= k:
                break
        for x in range(r + 1, len(grid)):
            D += 1
            if grid[x][c] >= k:
                break
        t = max(t, L * R * U * D)
print(t)
