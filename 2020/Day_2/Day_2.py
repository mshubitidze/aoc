input_lines = [i.strip().split(" ") for i in open("input.prod")]

inp_arr = []
for i in input_lines:
    n = [int(x) for x in i[0].split("-")]
    l = i[1][0]
    s = i[2]
    inp_arr.append([n, l, s])

# print(inp_arr)

valid = 0
for i in inp_arr:
    count = i[2].count(i[1])
    min = i[0][0]
    max = i[0][1]
    if count >= min and count <= max:
        valid += 1

valid2 = 0
for i in inp_arr:
    if (i[2][i[0][0]-1] == i[1]) ^ (i[2][i[0][1]-1] == i[1]):
        valid2 += 1

print(valid2)
