input = open(0).read().strip().split("\n")
reports = [list(map(int, row.split(" "))) for row in input]


def check(report):
    inc_dec = sorted(report) == report or sorted(report)[::-1] == report
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if diff < 1 or diff > 3:
            return False
    return inc_dec


ans = 0
for report in reports:
    if check(report):
        ans += 1
    else:
        for i in range(len(report)):
            curr = report[:i] + report[i + 1 :]
            if check(curr):
                ans += 1
                break

print(ans)
