from itertools import product

input = open(0).read().splitlines()


def compute_all_variations(numbers):
    operations = list(
        product(
            ["+", "*", "||"],
            repeat=len(numbers) - 1,
        )
    )
    results = set()
    for ops in operations:
        result = numbers[0]
        expression = str(numbers[0])
        for i, op in enumerate(ops):
            if op == "+":
                result += numbers[i + 1]
            elif op == "*":
                result *= numbers[i + 1]
            elif op == "||":
                result = int(str(result) + str(numbers[i + 1]))
            expression += f" {op} {numbers[i + 1]}"
        results.add(result)
    return results


sum = 0
for line in input:
    val = int(line.split(": ")[0])
    numbers = [int(n) for n in line.split(":")[1].split()]
    variations = compute_all_variations(numbers)
    if val in variations:
        sum += val

print(sum)
