def new_times(times):
    f = times[0]
    n_times = []
    for i in times[1:]:
        pair = []
        c = 0 - f[1]
        while len(pair) < 2:
            c += f[0]
            if (c + i[1]) % i[0] == 0:
                pair.append(c)
        n_times.append((pair[1] - pair[0], pair[0]))
    return n_times

f = open("inputd13", "r")
arrival = int(f.readline())
timetable = f.readline().split(",")
f.close()
times = []
for i in timetable:
    if i != "x":
        times.append(int(i))
wait = [(i - (arrival % i), i) for i in times]
next = min(wait)
print(next[0] * next[1]) # 13.1
times = []
for i in range(len(timetable)):
    if timetable[i] != "x":
        t = int(timetable[i])
        times.append((t, i))
while len(times) > 1:
    times = new_times(times)
print(times[0][0] - times[0][1]) # 13.2