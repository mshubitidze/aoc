# data = open(0).read()


data = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""


def get_dir(direction, instruction):
    if instruction == "R":
        if direction == "+x":
            return "-y"
        elif direction == "-x":
            return "+y"
        elif direction == "-y":
            return "-x"
        elif direction == "+y":
            return "+x"
    elif instruction == "L":
        if direction == "+x":
            return "+y"
        elif direction == "-x":
            return "-y"
        elif direction == "-y":
            return "+x"
        elif direction == "+y":
            return "-x"


def move_forward(x, y, direction, G):
    if direction == "+x":
        if G[x + 1][y] == "#":
            return x, y
        elif G[x + 1][y] == " ":
            G[x + 1][y] = "X"
            return x + 1, y
    elif direction == "+y":
        if G[x][y + 1] == "#":
            return x, y
        elif G[x][y + 1] == " ":
            G[x][y + 1] = "X"
            return x, y + 1
    elif direction == "-x":
        if G[x - 1][y] == "#":
            return x, y
        elif G[x - 1][y] == " ":
            G[x - 1][y] = "X"
            return x - 1, y
    elif direction == "-y":
        if G[x][y - 1] == "#":
            return x, y
        elif G[x][y - 1] == " ":
            G[x][y - 1] = "X"
            return x, y - 1


G, instr = data.split("\n\n")
G = G.split("\n")

x, y = 8, 0
direction = "+x"

for instruction in instr:
    if instruction.isdigit():
        for i in range(int(instruction)):
            x, y = move_forward(x, y, direction, G)
    else:
        direction = get_dir(direction, instruction)

for row in G:
    print(row)
