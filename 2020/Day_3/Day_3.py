input_lines = [i.strip() for i in open("input.prod")]

len_row = len(input_lines[0])

# Problem 2
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

ans = 1
for (dc,dr) in slopes:
    r = 0
    c = 0
    score = 0
    while r+1 < len(input_lines):
        c += dc
        r += dr
        if input_lines[r][c%len_row] == '#':
            score += 1
    ans *= score
print(ans)

# # Problem 1
# row = 0
# trees = 0
# row_index = 0
# col_index = 0
# while row_index < len(input_lines):
#     if input_lines[row_index][col_index] == "#":
#         trees += 1
#     if col_index + 3 >= len_row:
#         row_index += 1
#         col_index = (col_index + 3) - len_row
#     else:
#         row_index += 1
#         col_index += 3

# print(trees)
