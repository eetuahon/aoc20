c = 0
f = open("inputd02", "r")
for x in f:
    cut = x.split()
    lim = cut[0].split("-")
    find = cut[1][:1]
    many = cut[2].count(find)
    if many >= int(lim[0]) and many <= int(lim[1]):
        c += 1
f.seek(0)
print(c)

c = 0
for x in f:
    cut = x.split()
    pos = cut[0].split("-")
    find = cut[1][:1]
    first = int(pos[0])
    last = int(pos[1])
    if cut[2].count(find, first - 1, first) == 1 and cut[2].count(find, last - 1, last) != 1:
        c += 1
    elif cut[2].count(find, first - 1, first) != 1 and cut[2].count(find, last - 1, last) == 1:
        c += 1
f.close()
print(c)