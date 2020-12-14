def masked(string):
    bl = []
    wh = []
    for i in range(len(string)):
        if string[i] == "1":
            bl.append(i)
        elif string[i] == "0":
            wh.append(i)
    return (bl, wh)

data = []
values = dict()
f = open("inputd14", "r")
for x in f:
    x = x.replace("\n", "")
    row = x.split(" ")
    if row[0] == "mask":
        data.append(("mask", row[2][::-1]))
    else:
        data.append((row[0], int(row[2])))
f.close()
mask = []
for i in data:
    if i[0] == "mask":
        mask = masked(i[1])
    else:
        c = i[1]
        for j in mask[0]:
            c = c|(1<<j)
        for j in mask[1]:
            if c&(1<<j) != 0:
                c = c^(1<<j)
        values[i[0]] = c
print(sum(values.values())) # 14.1