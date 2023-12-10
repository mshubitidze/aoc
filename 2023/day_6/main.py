input = [int("".join(x.split()[1:])) for x in open(0).readlines()]

input = [[input[0], input[1]]]

a = []
for game in input:
    ways = 0
    for i in range(game[0]):
        distance = (game[0] - i) * i
        if distance > game[1]:
            ways += 1
    a.append(ways)

ans = 1
for i in a:
    ans *= i

print(ans)
