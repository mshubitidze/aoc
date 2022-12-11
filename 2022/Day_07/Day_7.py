cwd = root = {}
stack = []

for line in open('input.prod'):
    line = line.strip()
    if line[0] == "$":
        if line[2] == "c":
            dir = line[5:]
            if dir == "/":
                cwd = root
                stack = []
            elif dir == "..":
                cwd = stack.pop()
            else:
                if dir not in cwd:
                    cwd[dir] = {}
                stack.append(cwd)
                cwd = cwd[dir]
    else:
        x, y = line.split()
        if x == "dir":
            if y not in cwd:
                cwd[y] = {}
        else:
            cwd[y] = int(x)

# print(root)

# Problem #1
def solve(dir = root):
    if type(dir) == int:
        return (dir, 0)
    size = 0
    ans = 0
    for child in dir.values():
        s, a = solve(child)
        size += s
        ans += a
    if size <= 100000:
        ans += size
    return (size, ans)

print(solve()[1])

# Problem #2
def size(dir = root):
    if type(dir) == int:
        return dir
    return sum(map(size, dir.values()))

t = size() - 40_000_000

def solve2(dir = root):
    ans = float("inf")
    if size(dir) >= t:
        ans = size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        q = solve2(child)
        ans = min(ans, q)
    return ans

print(solve2())

