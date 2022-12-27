ids = open(0).read().splitlines()

seen = []
for i in range(len(ids)):
    c = []
    for j in range(len(ids[i])):
        ind = ids[i][:j] + ids[i][j+1:]
        if ind in seen:
            print(ind)
            exit(0)
        else:
            c.append(ind)
    seen += c

# twos = 0
# threes = 0

# for id in ids:
#     twice = False
#     thrice = False
#     for i in set([*id]):
#         if id.count(i) == 2 and not twice:
#             twos += 1
#             twice = True
#         if id.count(i) == 3 and not thrice:
#             threes += 1
#             thrice = True
        
# print(twos * threes)
