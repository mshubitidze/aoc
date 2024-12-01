input = open(0).read().splitlines()

a = []
b = []

for i in input:
    a.append(i.split()[0])
    b.append(i.split()[1])

ans = 0

for i in a:
    ans += int(i) * b.count(i)

print(ans)

# part 1
# a.sort()
# b.sort()
# ans = 0
# for i in range(len(a)):
#     ans += abs(int(a[i]) - int(b[i]))
# print(ans)
