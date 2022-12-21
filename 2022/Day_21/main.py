import sympy

monkeys = {"humn": sympy.Symbol("x")}

x = [line.strip() for line in open(0)]

ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

for line in x:
    name, expr = line.split(": ")
    if name in monkeys:
        continue
    if expr.isdigit():
        monkeys[name] = sympy.Integer(expr)
    else:
        left, op, right = expr.split()
        if left in monkeys and right in monkeys:
            if name == "root":
                print(sympy.solve(monkeys[left] - monkeys[right]))
                break
            monkeys[name] = ops[op](monkeys[left], monkeys[right])
        else:
            x.append(line)
