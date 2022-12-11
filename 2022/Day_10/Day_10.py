lines = [i.strip() for i in open("input.prod")]

G = [["." for _ in range(40)] for _ in range(6)]
ans = 0
x = 1
t = -1

cycles = [20, 60, 100, 140, 180, 220]

for line in lines:
    words = line.split()
    if words[0] == "noop":
        t += 1
        G[(t // 40)][t % 40] = "#" if abs(x - (t % 40)) <= 1 else " "
        if t in cycles:
            ans += x * t
    elif words[0] == "addx":
        t += 1
        G[(t // 40)][t % 40] = "#" if abs(x - (t % 40)) <= 1 else " "
        if t in cycles:
            ans += x * t
        t += 1
        G[(t // 40)][t % 40] = "#" if abs(x - (t % 40)) <= 1 else " "
        if t in cycles:
            ans += x * t
        x += int(words[1])

print(ans)
for r in range(6):
    print("".join(G[r]))
