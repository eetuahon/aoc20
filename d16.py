req = dict()
mine = []
others = []
names = []
f = open("inputd16", "r")
for r in f:
    if len(r) == 1:
        break
    r = r.replace("\n", "")
    #values = r.split(" ")
    row = r.split(": ")
    values = row[1].split(" or ")
    ok = set()
    first = [int(i) for i in values[0].split("-")]
    last = [int(i) for i in values[1].split("-")]
    for i in range(first[0], first[1] + 1):
        ok.add(i)
    for i in range(last[0], last[1] + 1):
        ok.add(i)
    req[row[0]] = ok
    names.append(row[0])
f.readline()
mine = f.readline().split(",")
mine = [int(i) for i in mine]
f.readlines(2)
for r in f:
    ticket = r.split(",")
    others.append([int(t) for t in ticket])
f.close()
sum = 0
valids = []
oks = set()
for i in req.values():
    oks.update(i)
for i in others:
    valid = True
    for j in i:
        if j not in oks:
            sum += j
            valid = False
    if valid:
        valids.append(i)
print(sum) # 16.1
pos = []
for i in range(len(names)):
    pos.append(names[:])
for t in valids:
    for i in range(len(names)):
        p = pos[i]
        if len(p) == 1:
            continue
        for j in p:
            if t[i] not in req.get(j):
                p.remove(j)
ind = dict()
while len(ind) < len(names):
    for i in range(len(names)):
        if len(pos[i]) == 1:
            n = pos[i][0]
            ind[n] = i
            for j in pos:
                if n in j: j.remove(n)
take = []
for x in ind.keys():
    if "departure" in x: take.append(ind[x])
prod = 1
for i in take:
    prod *= mine[i]
print(prod) # 16.2