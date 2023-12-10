opening = ["[", "{", "(", "<"]
closing = ["]", "}", ")", ">"]
table = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

lines = []

total = 0

for line in open(0).readlines():
    lines.append(line.strip())

legal = []
for line in lines:
    open = []
    l = False
    b = False
    for i in range(len(line)):
        if b == True:
            b = False
            break
        else:
            if line != lines[0]:
                legal.append(line)
        if line[i] in closing:
            if open[-1] != opening[closing.index(line[i])]:
                total += table[line[i]]
                b = True
                break
            else:
                open.pop(-1)
        else:
            open.append(line[i])

print(legal)
