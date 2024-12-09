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

possible_positions = [
    (i, j)
    for i in range(len(input))
    for j in range(len(input[i]))
    if input[i][j] != "#" and input[i][j] != "^"
]


def replace_character_at_pos(grid, pos):
    new_grid = grid[:]
    i, j = pos
    new_grid[i] = new_grid[i][:j] + "#" + new_grid[i][j + 1 :]
    return new_grid


def check_loops(grid, curr_pos):
    visited: set[tuple[str, tuple[int, int]]] = {("up", curr_pos)}
    directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
    turn_order = ["up", "right", "down", "left"]
    dir_idx = 0

    while curr_pos not in edges:
        dx, dy = directions[turn_order[dir_idx]]
        next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)

        if grid[next_pos[0]][next_pos[1]] == "#":
            dir_idx = (dir_idx + 1) % 4
        else:
            current = (turn_order[dir_idx], next_pos)
            if (current) in visited:
                return True
            visited.add(current)
            curr_pos = next_pos


res = []
for pos in possible_positions:
    new_grid = replace_character_at_pos(input, pos)
    res.append(check_loops(new_grid, curr_pos))

print(len([i for i in res if i == True]))
