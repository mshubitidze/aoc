nums = [int(i) for i in open("input.prod")]

for i in nums:
    for j in nums:
        if 2020 - i - j in nums:
            print(i * j * (2020 - i - j)) 


