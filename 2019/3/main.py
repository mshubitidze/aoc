wires = [wire_str.split(",") for wire_str in open(0).read().splitlines()]

points = []

for wire in wires:
    x = 0
    y = 0
    l1 = []
    for point in wire:
        dir = point[0]
        step = int(point[1:])
        if dir == "U":
            l1.append([x, (y, y + step)])
            y += step
        elif dir == "R":
            l1.append([(x, x + step), y])
            x += step
        elif dir == "D":
            l1.append([x, (y, y - step)])
            y -= step
        elif dir == "L":
            l1.append([(x, x - step), y])
            x -= step
    points.append(l1)


print(points)
