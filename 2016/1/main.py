directions = open(0).read().split(", ")

x = y = 0
c = "N"
seen = []
for direction in directions:
    d, n = direction[0], direction[1:]
    if c == "N":
        if d == "R":
            c = "E"
            x += int(n)
        else:
            c = "W"
            x -= int(n)
    elif c == "S":
        if d == "R":
            c = "W"
            x -= int(n)
        else:
            c = "E"
            x += int(n)
    elif c == "E":
        if d == "R":
            c = "S"
            y -= int(n)
        else:
            c = "N"
            y += int(n)
    elif c == "W":
        if d == "R":
            c = "N"
            y += int(n)
        else:
            c = "S"
            y -= int(n)
    if abs(x) + abs(y) in seen:
        print(abs(x) + abs(y))
    else:
        seen.append(abs(x) + abs(y))
