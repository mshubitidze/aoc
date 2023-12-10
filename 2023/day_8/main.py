import math

# p2
steps, _, *rest = open(0).read().splitlines()


def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)


network = {}
for line in rest:
    pos, targets = line.split(" = ")
    network[pos] = targets.strip(")(").split(", ")

all = [x for x in network if x[-1] == "A"]

cycles = []
for current in all:
    cycle = []
    current_steps = steps
    step_count = 0
    first_z = None

    while True:
        while step_count == 0 or not current[-1] == "Z":
            step_count += 1
            current = network[current][0 if current_steps[0] == "L" else 1]
            current_steps = current_steps[1:] + current_steps[0]
        cycle.append(step_count)
        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break
    cycles.append(cycle)

nums = [x[0] for x in cycles]
ans = nums.pop()
for num in nums:
    ans = lcm(ans, num)

print(ans)

# p1
# steps, _, *rest = open(0).read().splitlines()
#
# network = {}
# for line in rest:
#     pos, targets = line.split(" = ")
#     network[pos] = targets[1:-1].split(", ")
#
# step_count = 0
# current = "AAA"
# while current != "ZZZ":
#     step_count += 1
#     current = network[current][0 if steps[0] == "L" else 1]
#     steps = steps[1:] + steps[0]
#
# print(step_count)
