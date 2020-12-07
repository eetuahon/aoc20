def find_bags(st, di, se):
    bags = di.get(st, [])
    for b in bags:
        if b not in se:
            find_bags(b, di, se)
        se.add(b)

def in_bags(di, b):
    bags = di.get(b, 0)
    if bags[0] == 0:
        return 1
    else:
        c = 0
        for x in bags:
            c += in_bags(di, x)
        return 1 + c

bs = dict()
ins = dict()
out = set()
f = open("inputd07", "r")
for x in f:
    x = x.replace("bags", "bag")
    b = x.split(" contain ")
    b[1] = b[1].rstrip()
    b[1] = b[1].replace(".", "")
    bag = b[1].split(", ")
    for y in bag:
        y = y[2:]
        if y in bs.keys():
            bs[y].append(b[0])
        else:
            bs[y] = []
            bs[y].append(b[0])
    ins[b[0]] = []
    for y in bag:
        if y == "no other bag":
            ins[b[0]].append(0)
        else:
            times = int(y[0:1])
            for i in range(times):
                ins[b[0]].append(y[2:])
f.close()
find_bags("shiny gold bag", bs, out)
print(len(out)) # 07.1
print(in_bags(ins, "shiny gold bag") - 1) # 07.2, shiny gold bag manually excluded