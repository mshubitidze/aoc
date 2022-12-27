input = [int(x) for x in open(0).read().splitlines()]

fq = 0
seen = []

while True:
    for i in input:
        seen.append(fq)
        fq += i
        if fq in seen:
            print(fq)
            exit(0)
        print(fq)
