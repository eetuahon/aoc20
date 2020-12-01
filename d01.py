ns = []
f = open("d01_input", "r")
for x in f:
  n = int(x)
  if (2020 - n) in ns:
      print(n * (2020 - n))
      break
  else:
      ns.append(n)

f.close()