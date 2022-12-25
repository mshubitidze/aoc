SNAFU = [x.strip() for x in open(0).read().splitlines()]

sum = 0

def convert_snafu(n):
    n = n[::-1]
    dec = 0
    for i in range(len(n)):
        if n[i] == "-":
            snafu = -1
        elif n[i] == "=":
            snafu = -2
        else:
            snafu = int(n[i])
        dec += snafu * 5 ** i
    return dec


for i in SNAFU:
    sum += convert_snafu(i)

output = ""

while sum:
    rem = sum % 5
    sum //= 5
    
    if rem <= 2:
        output = str(rem) + output
    else:
        output = "   =-"[rem] + output
        sum += 1

print(output)
