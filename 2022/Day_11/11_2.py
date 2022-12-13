import sys
import math

input = """Monkey 0:
  Starting items: 56, 56, 92, 65, 71, 61, 79
  Operation: new = old * 7
  Test: divisible by 3
    If true: throw to monkey 3
    If false: throw to monkey 7

Monkey 1:
  Starting items: 61, 85
  Operation: new = old + 5
  Test: divisible by 11
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 2:
  Starting items: 54, 96, 82, 78, 69
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 0
    If false: throw to monkey 7

Monkey 3:
  Starting items: 57, 59, 65, 95
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 1

Monkey 4:
  Starting items: 62, 67, 80
  Operation: new = old * 17
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 6

Monkey 5:
  Starting items: 91
  Operation: new = old + 7
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 4

Monkey 6:
  Starting items: 79, 83, 64, 52, 77, 56, 63, 92
  Operation: new = old + 6
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 7:
  Starting items: 50, 97, 76, 96, 80, 56
  Operation: new = old + 3
  Test: divisible by 13
    If true: throw to monkey 3
    If false: throw to monkey 5"""

M = []
OP = []
DIV = []
TRUE = []
FALSE = []

for monkey in input.split("\n\n"):
    id_, items, op, test, true, false = monkey.split("\n")
    M.append([int(i) for i in items.split(":")[1].split(",")])
    words = op.split()
    op = "".join(words[-3:])
    OP.append(lambda old, op=op: eval(op))
    DIV.append(int(test.split()[-1]))
    TRUE.append(int(true.split()[-1]))
    FALSE.append(int(false.split()[-1]))

lcm = 1
for x in DIV:
    lcm = lcm * x // math.gcd(lcm, x)

C = [0 for _ in range(len(M))]
for _ in range(10000):
    for i in range(len(M)):
        for item in M[i]:
            C[i] += 1
            item = (OP[i](item)) % lcm
            if item % DIV[i] == 0:
                M[TRUE[i]].append(item)
            else:
                M[FALSE[i]].append(item)
        M[i] = []

print(sorted(C)[-1] * sorted(C)[-2])
