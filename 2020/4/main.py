"""
"byr", (Birth Year)
"iyr", (Issue Year)
"eyr", (Expiration Year)
"hgt", (Height)
"hcl", (Hair Color)
"ecl", (Eye Color)
"pid", (Passport ID)
"cid", (Country ID)
"""
passports_str = open(0).read().strip().split("\n\n")

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid = 0

valids = []

for passport in passports_str:
    if all(key in passport for key in keys):
        valid += 1
        valids.append(passport)

passports = [x.split() for x in valids]
ans = 0
good = []

def byr(v):
    return len(v) == 4 and int(v) >= 1920 and int(v) <= 2002

def iyr(v):
    return len(v) == 4 and int(v) >= 2010 and int(v) <= 2020

def eyr(val):
    return len(val) == 4 and int(val) >= 2020 and int(val) <= 2030

def hgt(val):
    if "in" in val:
        if len(val.split("in")) == 2 and int(val.split("in")[0]) >= 59 and int(val.split("in")[0]) <= 76:
            return True
    elif "cm" in val:
        if len(val.split("cm")) == 2 and int(val.split("cm")[0]) >= 150 and int(val.split("cm")[0]) <= 193:
            return True
    else:
        return False

def hcl(val):
    return len(val) == 7 and all(x in "abcdef0123456789#" for x in val)

def ecl(val):
    return val in "amb blu brn gry grn hzl oth".split()
        
def pid(val):
    if len(val) != 9:
        return False
    for i in val:
        if i not in "0123456789":
            return False
    return True

for passport in passports:
    v = 0
    for item in passport:
        key, val = item.split(":")
        if key == "byr":
            if byr(val):
                v += 1
        elif key == "iyr":
            if iyr(val):
                v += 1
        elif key == "eyr":
            if eyr(val):
                v += 1
        elif key == "hgt":
            if hgt(val):
                v += 1
        elif key == "hcl":
            if hcl(val):
                v += 1
        elif key == "ecl":
            if ecl(val):
                v += 1
        elif key == "pid":
            if pid(val):
                v += 1
    if v == 7:
        good.append(passport)

print(len(good))
