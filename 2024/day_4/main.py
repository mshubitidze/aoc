input = open(0).read().strip().splitlines()

# [0,0] [0,1] [0,2] [0,3]
# [0,0] [1,0] [2.0] [3,0]
# [0,0] [1,1] [2,2] [3,3]

# M.S
# .A.
# M.S


"""  
MSAMS
MMASS
SSAMM
SMASM

.F.S......
..A..FSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

"""

x_words = ["MSAMS", "MMASS", "SSAMM", "SMASM"]


def get_x(grid, x, y):
    x = [[x, y], [x, y + 2], [x + 1, y + 1], [x + 2, y], [x + 2, y + 2]]
    word = "".join(grid[indices[0]][indices[1]] for indices in x)
    if word in x_words:
        return True


found = []

for i in range(len(input)):
    for j in range(len(input[0])):
        if i + 3 <= len(input) and j + 3 <= len(input[0]):
            if get_x(input, i, j):
                found.append([i, j])

print(found, len(found))

""" part 1 """
# words = ["XMAS", "SAMX"]
#
# rlen, clen = len(input), len(input[0])
# count = 0
#
# for j in input:
#     for i in range(clen - 3):
#         word = "".join(j[i : i + 4])
#         if word in words:
#             count += 1
#
# for i in range(clen):
#     for j in range(rlen - 3):
#         word = "".join(input[j + k][i] for k in range(4))
#         if word in words:
#             count += 1
#
# for i in range(rlen - 3):
#     for j in range(clen - 3):
#         word = "".join(input[i + k][j + k] for k in range(4))
#         if word in words:
#             count += 1
#
# for i in range(rlen - 3):
#     for j in range(3, clen):
#         word = "".join(input[i + k][j - k] for k in range(4))
#         if word in words:
#             count += 1
#
#
# print(count)
