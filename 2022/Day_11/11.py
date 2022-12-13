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


lines = input.strip().split("\n\n")


class Monkey:
    def __init__(self, starting_items, operation, test, if_true, if_false):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.count = 0

    def inspect_and_throw_items(self, monkeys):
        for item in self.items:
            self.count += 1
            result = eval(self.operation.replace("old", str(item)))
            # result = result // 3
            if result % self.test == 0:
                monkeys[self.if_true].items.append(result)
            else:
                monkeys[self.if_false].items.append(result)
        self.items = []


monkeys = []

for i in lines:
    line = [j.strip() for j in i.split("\n")]
    starting_items = line[1].split(": ")[1].split(", ")
    operation = line[2].split(": ")[1][6:]
    test = int(line[3].split(" ")[-1])
    t = int(line[4].split(" ")[-1])
    f = int(line[5].split(" ")[-1])
    monkeys.append(Monkey(starting_items, operation, test, t, f))

for i in range(20):
    for monkey in monkeys:
        monkey.inspect_and_throw_items(monkeys)

for i, monkey in enumerate(monkeys):
    print(f"Monkey {i}: {monkey.count} inspections")
