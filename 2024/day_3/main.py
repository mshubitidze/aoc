import re

input = open(0).read().strip()

ans = 0
enabled = True

for match in re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", input):
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    elif enabled:
        x, y = map(int, match[4:-1].split(","))
        ans += x * y

print(ans)
