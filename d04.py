import re
c = 0
passlist = []
f = open("inputd04", "r")
pp = {}
for x in f:
    if len(x) == 1:
        passlist.append(pp)
        pp = {}
    line = x.split()
    for y in line:
        entry = y.split(":")
        pp.update({entry[0] : entry[1]})
passlist.append(pp)
f.close()
for p in passlist:
    if len(p) < 7:
        pass
    elif len(p) == 7 and p.get("cid", -1) == -1:
        c += 1
    elif len(p) == 8:
        c += 1
print(c) # 04.1
c = 0
for p in passlist:
    if len(p) < 7:
        pass
    pong = 0
    byr = int(p.get("byr", -1))
    if byr <= 2002 and byr >= 1920:
        pong += 1
    iyr = int(p.get("iyr", -1))
    if iyr <= 2020 and iyr >= 2010:
        pong += 1
    eyr = int(p.get("eyr", -1))
    if eyr <= 2030 and eyr >= 2020:
        pong += 1
    hcl = re.match("#[0-9a-f]{6}", p.get("hcl", "-"))
    if hcl:
        pong += 1
    ecl = re.match("amb|blu|brn|gry|grn|hzl|oth", p.get("ecl", "-"))
    if ecl:
        pong += 1
    hgt = re.search("in$|cm$", p.get("hgt", "-"))
    if hgt:
        h = int(hgt.string[0:-2])
        if hgt.string[-2:] == "cm" and h >= 150 and h <= 193:
            pong += 1
        if hgt.string[-2:] == "in" and h >= 59 and h <= 76:
            pong += 1
    pid = re.search("\d{9}", p.get("pid", "-"))
    if pid and len(pid.string) == 9:
        pong += 1
    if pong == 7:
        c += 1
print(c) # 04.2