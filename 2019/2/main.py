memory = list(map(int, open(0).read().split(",")))

memory[1] = 12
memory[2] = 4

pos = 0

for verb in range(100):
    for noun in range(100):
        if memory[0] == 19690720:
            print(100 * noun + verb)
            exit(0)
        else:
            m = memory[:]
            while True:
                memory[1] = noun
                memory[2] = verb
                x1 = memory[memory[pos + 1]]
                x2 = memory[memory[pos + 2]]
                y1 = memory[memory[pos + 3]]
                if memory[pos] == 99:
                    pos += 1
                    break
                elif memory[pos] == 2:
                    y1 = x1 * x2
                elif memory[pos] == 1:
                    y1 = x1 + x2
                print(pos)
