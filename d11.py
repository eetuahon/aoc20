def occupied_adj(y, x):
    c = 0
    if x > 0:
        if seats[y][x - 1] == "#":
            c += 1
    if y > 0:
        if seats[y - 1][x] == "#":
            c += 1
    if x > 0 and y > 0:
        if seats[y - 1][x - 1] == "#":
            c += 1
    if x > 0 and y < rows - 1:
        if seats[y + 1][x - 1] == "#":
            c += 1
    if x < cols - 1 and y > 0:
        if seats[y - 1][x + 1] == "#":
            c += 1
    if x < cols - 1:
        if seats[y][x + 1] == "#":
            c += 1
    if y < rows - 1:
        if seats[y + 1][x] == "#":
            c += 1
    if x < cols - 1 and y < rows - 1:
        if seats[y + 1][x + 1] == "#":
            c += 1
    return c

def occupied_adj_seen(y, x):
    c = 0
    a = x
    while a > 0:
        a -= 1
        if seats2[y][a] == "#":
            c += 1
            break
        elif seats2[y][a] == "L":
            break
    b = y
    while b > 0:
        b -= 1
        if seats2[b][x] == "#":
            c += 1
            break
        elif seats2[b][x] == "L":
            break
    a = x
    b = y
    while a > 0 and b > 0:
        a -= 1
        b -= 1
        if seats2[b][a] == "#":
            c += 1
            break
        elif seats2[b][a] == "L":
            break
    a = x
    b = y
    while a > 0 and b < rows - 1:
        a -= 1
        b += 1
        if seats2[b][a] == "#":
            c += 1
            break
        elif seats2[b][a] == "L":
            break
    a = x
    b = y
    while a < cols - 1 and b > 0:
        b -= 1
        a += 1
        if seats2[b][a] == "#":
            c += 1
            break
        elif seats2[b][a] == "L":
            break
    a = x
    while a < cols - 1:
        a += 1
        if seats2[y][a] == "#":
            c += 1
            break
        elif seats2[y][a] == "L":
            break
    b = y
    while b < rows - 1:
        b += 1
        if seats2[b][x] == "#":
            c += 1
            break
        elif seats2[b][x] == "L":
            break
    a = x
    b = y
    while a < cols - 1 and b < rows - 1:
        a += 1
        b += 1
        if seats2[b][a] == "#":
            c += 1
            break
        elif seats2[b][a] == "L":
            break
    return c

f = open("inputd11", "r")
seats = []
seats2 = []
for x in f:
    x = x.replace("\n", "")
    seats.append(list(x))
    seats2.append(list(x))
f.close()
cols = len(seats[0])
rows = len(seats)
occup = 0
changes = -1
while changes != 0:
    swaps = []
    for y in range(rows):
        for x in range(cols):
            s = seats[y][x]
            if s == ".":
                pass
            if s == "L" and occupied_adj(y, x) == 0:
                swaps.append((y, x))
            elif s == "#" and occupied_adj(y, x) >= 4:
                swaps.append((y, x))
    changes = len(swaps)
    for s in swaps:
        y = s[0]
        x = s[1]
        if seats[y][x] == "L":
            seats[y][x] = "#"
            occup += 1
        else:
            seats[y][x] = "L"
            occup -= 1
print(occup) # 11.1
occup = 0
changes = -1
while changes != 0:
    swaps = []
    for y in range(rows):
        for x in range(cols):
            s = seats2[y][x]
            if s == ".":
                pass
            if s == "L" and occupied_adj_seen(y, x) == 0:
                swaps.append((y, x))
            elif s == "#" and occupied_adj_seen(y, x) >= 5:
                swaps.append((y, x))
    changes = len(swaps)
    for s in swaps:
        y = s[0]
        x = s[1]
        if seats2[y][x] == "L":
            seats2[y][x] = "#"
            occup += 1
        else:
            seats2[y][x] = "L"
            occup -= 1
print(occup) # 11.2