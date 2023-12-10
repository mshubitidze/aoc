import re


input = open(0).read().strip().splitlines()

nums = [
    re.findall(
        r"(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))", x
    )
    for x in input
]

m = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

n = []

for p in nums:
    h = [x if len(x) == 1 else m[x] for x in p]
    n.append(h)

s = [x[0] + x[-1] if len(x) > 1 else x[0] + x[0] for x in n]

print(sum([int(x) for x in s]))
