seats = []
f = open("inputd05", "r")
for x in f:
    x = x.replace("B", "1")
    x = x.replace("F", "0")
    x = x.replace("R", "1")
    x = x.replace("L", "0")
    row = int(x[0:7], 2)
    col = int(x[7:10], 2)
    sid = 8 * row + col
    seats.append(sid)
f.close()
print(max(seats)) # 05.1
for i in range(min(seats), max(seats)):
    if not i in seats:
        print(i) # 05.2