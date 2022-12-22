input = open(0)
str_num_arr = [
    [y.split(",") for y in x.split(" -> ")] for x in input.read().splitlines()
]
coordinates = [[[int(i) for i in y] for y in x] for x in str_num_arr]

max_num = 4000

# grid = [[0 for _ in range(max_num)] for _ in range(max_num)]

grid = {}

for coordinate in coordinates:
    x1 = coordinate[0][0]
    x2 = coordinate[1][0]
    y1 = coordinate[0][1]
    y2 = coordinate[1][1]

    dx = x2 - x1
    dy = y2 - y1
    if dx: dx = dx // abs(dx)
    if dy: dy = dy // abs(dy)
    x = x1
    y = y1
    while True:
        grid[(x, y)] = grid.get((x, y), 0) + 1
        if x == x2 and y == y2:
            break
        x += dx
        y += dy

t = 0
for v in grid.values():
    if v > 1:
        t += 1

print(t)
