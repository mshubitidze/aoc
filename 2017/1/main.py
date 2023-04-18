input = open(0).read().strip().split("\n")

arrs = []

for line in input:
    arr = []
    half = len(line) // 2
    for i in range(half):
        if i >= half:
            idx = (i + half) % (half // 2)
        else:
            idx = i + half
        if line[i] == line[idx]:
            arr.append(int(line[i]))
    arrs.append(arr)

print([sum(arr) for arr in arrs])
