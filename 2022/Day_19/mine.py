import re

blueprints = open(0).read().splitlines()

"""
geode-cracking robots
obsidian-collecting robots
clay-collecting robots
ore-collecting robots
"""

res = []

for blueprint in blueprints:
    T = 24
    ocr = 1
    ccr = obcr = gcr = ore = clay = obsidian = cracked = 0

    x = list(map(int, re.findall(r"(\d+)", blueprint)))
    num, ocr_cost, ccr_cost, obcr_cost, gcr_cost = (
        x[0],
        x[1],
        x[2],
        x[3:5],
        x[5:],
    )
    print(f"Blueprint #{num}")
    while T > 0:
        if ore >= gcr_cost[0] and obsidian >= gcr_cost[1]:
            gcr += 1
            ore -= gcr_cost[0]
            obsidian -= gcr_cost[1]
            T -= 1
            print(f"Built a geode collecting robot, current count: {gcr}")
        elif ore >= obcr_cost[0] and clay >= obcr_cost[1]:
            obcr += 1
            ore -= obcr_cost[0]
            clay -= obcr_cost[1]
            T -= 1
            print(f"Built an obsidian collecting robot, current count: {obcr}")
        elif ore >= ccr_cost and ccr < 3:
            ccr += 1
            ore -= ccr_cost
            T -= 1
            print(f"Built a clay collecting robot, current count: {ccr}")
        elif ore >= ocr_cost and ocr < 3:
            ocr += 1
            ore -= ocr_cost
            T -= 1
            print(f"Built an ore collecting robot, current count: {ocr}")
        # print(
        #     f"Time Left: {T}\n",
        #     f"robots: {ocr}, {ccr}, {obcr}, {gcr}\n",
        #     f"resources: {ore}, {clay}, {obsidian}\n",
        #     f"cracked: {cracked}\n",
        # )
        ore += ocr
        clay += ccr
        obsidian += obcr
        cracked += gcr
        T -= 1
        print(f"Time Left: {T}")
        print(f"Resource count: {ore} ore, {clay} clay, {obsidian} obsidian")
        print(f"Cracked geodes: {cracked}\n")
    res.append(cracked)

print(res)
