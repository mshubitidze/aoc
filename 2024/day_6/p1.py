input = open(0).read().splitlines()

curr_pos = [
    (i, j) for i, row in enumerate(input) for j, cell in enumerate(row) if cell == "^"
][0]

edges = set(
    [(0, i) for i in range(len(input[0]))]
    + [(len(input) - 1, i) for i in range(len(input[-1]))]
    + [(i, 0) for i in range(len(input))]
    + [(i, len(input[i]) - 1) for i in range(len(input))]
)

visited = {curr_pos}
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
turn_order = ["up", "right", "down", "left"]
dir_idx = 0

while curr_pos not in edges:
    dx, dy = directions[turn_order[dir_idx]]
    next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)

    if input[next_pos[0]][next_pos[1]] == "#":
        dir_idx = (dir_idx + 1) % 4
    else:
        visited.add(next_pos)
        curr_pos = next_pos

print(visited)
print(len(visited))
