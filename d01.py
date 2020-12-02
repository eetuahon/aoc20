ns = []
f = open("inputd01", "r")
for x in f:
  n = int(x)
  if (2020 - n) in ns:
      print(n * (2020 - n))
  else:
      ns.append(n)

ns2 = []
f.seek(0)
for x in f:
    n = int(x)
    for m in ns:
        if n + m < 2020 and n != m:
            tup = (n + m, n * m)
            if tup not in ns2:
                ns2.append(tup)
f.seek(0)
for x in f:
    n = int(x)
    for tup in ns2:
        if n + tup[0] == 2020:
            print(tup[1] * n)
            break
f.close()