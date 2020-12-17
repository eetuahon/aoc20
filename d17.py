def count_nbr(dot):
    x = dot[0]
    y = dot[1]
    z = dot[2]
    s = set()
    if len(dot) > 3: w = dot[3]
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if len(dot) == 3: s.add((i, j, k))
                else:
                    for l in range(w - 1, w + 2):
                        s.add((i, j, k, l))
    c = 0
    for d in s:
        if len(dot) < 4:
            if d in actives and d != dot: c += 1
        else:
            if d in actives4d and d != dot: c += 1
    return c

def check_these():
    ct = set()
    for i in range(limx[0] - 1, limx[1] + 2):
        for j in range(limy[0] - 1, limy[1] + 2):
            for k in range(limz[0] - 1, limz[1] + 2):
                ct.add((i, j, k))
    return ct

def check_these4d():
    ct = set()
    for i in range(limx[0] - 1, limx[1] + 2):
        for j in range(limy[0] - 1, limy[1] + 2):
            for k in range(limz[0] - 1, limz[1] + 2):
                for l in range(limw[0] - 1, limw[1] + 2):
                    ct.add((i, j, k, l))
    return ct

def activator(dot):
    c = count_nbr(dot)
    if dot in actives:
        if c == 2 or c == 3: return True
        else: return False
    else:
        if c == 3: return True
        else: return False

def activator4d(dot):
    c = count_nbr(dot)
    if dot in actives4d:
        if c == 2 or c == 3: return True
        else: return False
    else:
        if c == 3: return True
        else: return False

actives = set()
actives4d = set()
limx = (0, 0)
limy = (0, 0)
limz = (0, 0)
limw = (0, 0)
f = open("inputd17", "r")
y = 0
for r in f:
    x = 0
    row = list(r)
    for c in row:
        if c == "#":
            actives.add((x, y, 0))
            actives4d.add((x, y, 0, 0))
            if x < limx[0]: limx = (x, limx[1])
            if x > limx[1]: limx = (limx[0], x)
            if y < limy[0]: limy = (y, limy[1])
            if y > limy[1]: limy = (limy[0], y)
        x += 1
    y += 1
f.close()
many = 6
for i in range(many):
    next_actives = set()
    ct = check_these()
    for dot in ct:
        next = activator(dot)
        if next:
            next_actives.add(dot)
            if dot[0] < limx[0]: limx = (dot[0], limx[1])
            if dot[0] > limx[1]: limx = (limx[0], dot[0])
            if dot[1] < limy[0]: limy = (dot[1], limy[1])
            if dot[1] > limy[1]: limy = (limy[0], dot[1])
            if dot[2] < limz[0]: limz = (dot[2], limz[1])
            if dot[2] > limz[1]: limz = (limz[0], dot[2])
    actives = next_actives
print(len(actives)) # 17.1
for i in range(many):
    next_actives = set()
    ct = check_these4d()
    for dot in ct:
        next = activator4d(dot)
        if next:
            next_actives.add(dot)
            if dot[0] < limx[0]: limx = (dot[0], limx[1])
            if dot[0] > limx[1]: limx = (limx[0], dot[0])
            if dot[1] < limy[0]: limy = (dot[1], limy[1])
            if dot[1] > limy[1]: limy = (limy[0], dot[1])
            if dot[2] < limz[0]: limz = (dot[2], limz[1])
            if dot[2] > limz[1]: limz = (limz[0], dot[2])
            if dot[3] < limw[0]: limw = (dot[3], limw[1])
            if dot[3] > limw[1]: limw = (limw[0], dot[3])
    actives4d = next_actives
print(len(actives4d)) # 17.2