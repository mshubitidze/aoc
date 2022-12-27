from collections import defaultdict


N = [int(x) for x in open(0).read().strip().split(",")]

X = defaultdict(int)

for n in N:
    if n not in X:
        X[n] = 0
    X[n] += 1

for day in range(256):
    Y = defaultdict(int)
    for x, cnt in X.items():
        if x == 0:
            Y[6] += cnt
            Y[8] += cnt
        else:
            Y[x-1] += cnt
    X = Y

print(sum(X.values()))

# c = 0
# while c < 256:
#     print(c)
#     for i in range(len(fish)):
#         t = []
#         if fish[i] == 0:
#             fish[i] = 6
#             t.append(8)
#         else:
#             fish[i] -= 1
        
#         if t:
#             fish += t
#     c += 1
#     print(len(fish))
# print(len(fish))
