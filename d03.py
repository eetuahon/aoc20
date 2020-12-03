c = 0
map = []
f = open("inputd03", "r")
for x in f:
    map.append(list(x))
f.close()
rows = len(map)
cols = len(map[0]) - 1
x = 0
for y in range(rows):
    if map[y][x] == "#":
        c += 1
    x += 3
    if x >= cols:
        x = x % cols
print(c) # 03.1
counters = [0, c, 0, 0, 0]
xs = [0, 0, 0, 0, 0]
for y in range(rows):
    if map[y][xs[0]] == "#":
        counters[0] += 1
    if map[y][xs[2]] == "#":
        counters[2] += 1
    if map[y][xs[3]] == "#":
        counters[3] += 1
    if map[y][xs[4]] == "#" and y % 2 == 0:
        counters[4] += 1
    if y % 2 == 0:
        xs[4] += 1
    xs = [xs[0] + 1, xs[1], xs[2] + 5, xs[3] + 7, xs[4]]
    xs = [s % cols for s in xs]
print(counters[0] * counters[1] * counters[2] * counters[3] * counters[4]) # 03.2