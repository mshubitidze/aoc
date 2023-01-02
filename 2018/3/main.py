import re

claims = open(0).read().strip().splitlines()


data = []
for line in claims:
    nums = [int(n) for n in re.findall(r"\d+", line)]
    data.append(
        {
            "id": nums[0],
            "coordinates": [nums[1], nums[2]],
            "dimensions": [nums[3], nums[4]],
        }
    )


def get_coordinates(coordinates, dimensions):
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            yield str(x + coordinates[0]) + "," + str(y + coordinates[1])


def get_overlaps(data):
    overlaps = set()
    filled = set()
    for line in data:
        for coord in get_coordinates(line["coordinates"], line["dimensions"]):
            if coord in filled:
                overlaps.add(coord)
            else:
                filled.add(coord)
    return overlaps


def no_overlaps(coordinates, dimensions, overlaps):
    for coord in get_coordinates(coordinates, dimensions):
        if coord in overlaps:
            return False
    return True


def find_no_overlaps(data, overlaps):
    for line in data:
        if no_overlaps(line["coordinates"], line["dimensions"], overlaps):
            return line["id"]


overlaps = get_overlaps(data)
# Q1
print(len(overlaps))

# Q2
print(find_no_overlaps(data, overlaps))


# seen = {}
# count = 0

# points = {}

# for claim in claims:
#     elements = claim.split()
#     ID = int(elements[0][1:])
#     left, top = map(int, elements[2][:-1].split(","))
#     width, height = map(int, elements[-1].split("x"))

#     start = (left + 1, top + 1)
#     end = (left + 1 + width, top + 1 + height)

#     points[ID] = (start, end)

# recs = {}

# for id in points:
#     for id1 in points:
#         if id == id1:
#             break

#             x, y, x1, y1 = (
#                 points[id][0][0],
#                 points[id][0][1],
#                 points[id][1][0],
#                 points[id][1][1],
#             )
#
#             x2, y2, x3, y3 = (
#                 points[id1][0][0],
#                 points[id1][0][1],
#                 points[id1][1][0],
#                 points[id1][1][1],
#             )

#         if x >= x2 and y >= y2 and x1 <= x3 and y1 <= y3:

#     pass

# for item in points:
#     start = points[item][0]
#     end = points[item][1]

#     for x in range(start[0], end[0]):
#         for y in range(start[1], end[1]):
#             point = (x, y)
#             if item in recs:
#                 recs[item].append(point)
#             else:
#                 recs[item] = [(x, y)]

# broke = []
# for item in recs:
#     for item1 in recs:
#         if item == item1:
#             continue
#         for point in recs[item]:
#             if point in recs[item1]:
#                 broke.append(item)
#                 break

# print(broke)

# # # Part 1
# # for item in points:
# #     start = points[item][0]
# #     end = points[item][1]

# #     for x in range(start[0], end[0]):
# #         for y in range(start[1], end[1]):
# #             point = (x, y)
# #             if point in seen:
# #                 seen[point] += 1
# #             else:
# #                 seen[point] = 1


# # for item in seen:
# #     if seen[item] >= 2:
# #         count += 1
# #         print(item)

# # print(count)
