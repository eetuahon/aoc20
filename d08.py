def change(i, ar):
    d = ar[i]
    if d[0] == "nop":
        d = ("jmp", d[1])
    elif d[0] == "jmp":
        d = ("nop", d[1])
    ar[i] = d

f = open("inputd08", "r")
com = []
for x in f:
    x = x.replace("\n", "")
    y = x.split(" ")
    z = (y[0], int(y[1]))
    com.append(z)
f.close()
i = 0
c = 0
used = set()
changes = []
while (True):
    if i in used:
        break
    if com[i][0] == "nop":
        used.add(i)
        changes.append(i)
        i += 1
    elif com[i][0] == "acc":
        used.add(i)
        c += com[i][1]
        i += 1
    elif com[i][0] == "jmp":
        used.add(i)
        changes.append(i)
        i += com[i][1]
print(c) # 08.1
found = False
for x in changes:
    if found:
        break
    used = set()
    c = 0
    i = 0
    change(x, com)
    while (True):
        if i >= len(com):
            found = True
            break
        elif i in used:
            break
        if com[i][0] == "nop":
            used.add(i)
            changes.append(i)
            i += 1
        elif com[i][0] == "acc":
            used.add(i)
            c += com[i][1]
            i += 1
        elif com[i][0] == "jmp":
            used.add(i)
            changes.append(i)
            i += com[i][1]
    change(x, com)
print(c) # 08.2