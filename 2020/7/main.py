# input = [x.split(" bags contain ") for x in open(0).read().splitlines()]

# bags = {}

# for line in input:
#     bags[line[0]] = [[x.split()[0], " ".join(x.split()[1:-1])] if x != "no other bags." else [] for x in line[1].split(", ")]

# contains = []
# for k in bags:
#     for b in bags[k]:
#         for item in b:
#             if item == "shiny gold":
#                 contains.append(k)

# print(contains)

lines = open(0).read().splitlines()

bags = []
non = []
for line in lines:
    c = line.split(" bags ")
    if "shiny gold" in c[1]:
        bags.append(c[0])
    else:
        non.append(line)

ans = []
copy = ans
lmao = []
while True:
    for line in non:
        for bag in bags:
            c = line.split(" bags ")
            if bag in c[1:]:
                ans.append(c[0])
                break
    if copy == ans:
        print(ans)
        break


l = [
    [
        "pale yellow",
        "dim gold",
        "dull salmon",
        "dull purple",
        "muted indigo",
        "posh coral",
    ],
    [
        "mirrored cyan",
        "bright yellow",
        "dark magenta",
        "pale indigo",
        "pale blue",
        "dotted magenta",
        "faded teal",
        "posh maroon",
        "drab crimson",
        "clear beige",
        "mirrored lavender",
        "muted red",
        "wavy teal",
        "wavy crimson",
        "bright gold",
        "muted fuchsia",
        "faded red",
        "shiny chartreuse",
        "dotted teal",
        "shiny black",
        "clear blue",
    ],
    [
        "posh indigo",
        "wavy yellow",
        "drab brown",
        "dotted tomato",
        "vibrant coral",
        "shiny tan",
        "pale beige",
        "dull lavender",
        "striped crimson",
        "clear gray",
        "faded purple",
        "dotted purple",
        "clear salmon",
        "posh orange",
        "bright tomato",
        "striped black",
        "faded coral",
        "vibrant crimson",
        "light purple",
        "dotted crimson",
        "dark purple",
        "plaid silver",
        "clear lime",
        "dull violet",
        "dotted brown",
        "muted turquoise",
        "shiny cyan",
        "dull chartreuse",
        "wavy indigo",
        "wavy olive",
        "wavy silver",
        "bright gold",
        "bright crimson",
        "mirrored teal",
        "striped chartreuse",
        "clear teal",
        "dull black",
        "dim coral",
        "drab lime",
        "shiny purple",
        "striped olive",
        "muted beige",
        "dull maroon",
        "wavy orange",
        "wavy white",
    ],
]

kek = set()
for i in l:
    for j in i:
        kek.add(j)

print(len(list(kek)))
print(bags)
print(len(lines))
