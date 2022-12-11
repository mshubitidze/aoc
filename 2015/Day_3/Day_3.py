input = "yzbqklnj"


# MD5 hash formula

def md5hash(string):
    import hashlib
    return hashlib.md5(string.encode()).hexdigest()

i = 0
while True:
    to_hash = input + str(i)
    hashed = md5hash(to_hash)
    if hashed[:6] == "000000":
        print(i)
    i+=1


