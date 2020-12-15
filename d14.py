from itertools import combinations
import re
def masked(string):
    bl = []
    wh = []
    x = []
    for i in range(len(string)):
        if string[i] == "1":
            bl.append(i)
        elif string[i] == "0":
            wh.append(i)
        else:
            x.append(i)
    return (bl, wh, x)

def possibilities(ls, orig):
    p = []
    for i in range(len(ls)):
        p.append(1 << ls[i])
    ls = [(1 << i) for i in ls]
    out = sum([list(map(list, combinations(ls, i))) for i in range(len(ls) + 1)], [])
    return [sum(i) + orig for i in out]

data = []
values = dict()
values2 = dict()
f = open("inputd14", "r")
for x in f:
    x = x.replace("\n", "")
    row = x.split(" ")
    if row[0] == "mask":
        data.append(("mask", row[2][::-1]))
    else:
        n = re.search("\d+", row[0])
        data.append((int(n.group()), int(row[2])))
f.close()
mask = []
for i in data:
    if i[0] == "mask":
        mask = masked(i[1])
    else:
        c = i[1]
        orig = i[0]
        for j in mask[0]:
            c = c|(1<<j)
            orig = orig|(1<<j)
        for j in mask[1]:
            if c&(1<<j) != 0:
                c = c^(1<<j)
        for j in mask[2]:
            if orig&(1<<j) != 0:
                orig = orig^(1<<j)
        values[i[0]] = c
        pos = possibilities(mask[2], orig)
        for j in pos:
            values2[j] = i[1]
        
print(sum(values.values())) # 14.1
print(sum(values2.values())) # 14.2