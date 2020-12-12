f = open("inputd12", "r")
instr = []
for x in f:
    x = x.replace("\n", "")
    dir = x[0]
    val = int(x[1:])
    instr.append((dir, val))
f.close()
moves = [0, 0, 0, 0, 90] # N, E, S, W, °
for x in instr:
    c = x[0]
    num = x[1]
    if c == "N":
        moves[0] += num
    elif c == "E":
        moves[1] += num
    elif c == "S":
        moves[2] += num
    elif c == "W":
        moves[3] += num
    elif c == "R":
        moves[4] += num
    elif c == "L":
        moves[4] -= num
    elif c == "F":
        moves[4] %= 360
        dir = moves[4]
        if dir == 0:
            moves[0] += num
        elif dir == 90:
            moves[1] += num
        elif dir == 180:
            moves[2] += num
        elif dir == 270:
            moves[3] += num
n = abs(moves[0] - moves[2])
e = abs (moves[1] - moves[3])
print(n + e) # 12.1
moves = [0, 0] # N, E
wp = [1, 10] # N, E
for x in instr:
    c = x[0]
    num = x[1]
    if c == "N":
        wp[0] += num
    elif c == "E":
        wp[1] += num
    elif c == "S":
        wp[0] -= num
    elif c == "W":
        wp[1] -= num
    elif c == "R":
        times = int(num / 90)
        for i in range(times):
            a = wp[0]
            wp[0] = wp[1]
            wp[1] = a
            wp[0] *= -1
    elif c == "L":
        times = int(num / 90)
        for i in range(times):
            a = wp[0]
            wp[0] = wp[1]
            wp[1] = a
            wp[1] *= -1
    elif c == "F":
        moves[0] += num * wp[0]
        moves[1] += num * wp[1]
n = abs(moves[0])
e = abs (moves[1])
print(n + e) # 12.2