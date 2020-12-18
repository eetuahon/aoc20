def solve(row):
    while "(" in row:
        depth = 0
        a = row.find("(")
        for i in range(len(row)):
            if i >= len(row): continue
            if row[i] == "(": depth += 1
            if row[i] == ")": depth -= 1
            if row[i] == ")" and depth == 0:
                mid = str(solve(row[a + 1:i]))
                end = row[i + 1:len(row)]
                row = row[:a] + mid + end
                break
    return left_solve(row.split(" "))

def psolve(row):
    while "(" in row:
        depth = 0
        a = row.find("(")
        for i in range(len(row)):
            if i >= len(row): continue
            if row[i] == "(": depth += 1
            if row[i] == ")": depth -= 1
            if row[i] == ")" and depth == 0:
                mid = str(psolve(row[a + 1:i]))
                end = row[i + 1:len(row)]
                row = row[:a] + mid + end
                break
    return plus_solve(row.split(" * "))

def left_solve(ar):
    sol = int(ar[0])
    for i in range(1, len(ar), 2):
        if ar[i] == "+": sol += int(ar[i + 1])
        if ar[i] == "*": sol *= int(ar[i + 1])
    return sol

def plus_solve(ar):
    sol = 1
    for i in ar:
        times = i.split(" + ")
        sol *= sum([int(x) for x in times])
    return sol

rows = []
f = open("inputd18", "r")
for r in f:
    rows.append(r.replace("\n", ""))
f.close()
sums = []
for i in rows:
    s = solve(i)
    sums.append(s)
print(sum(sums)) # 18.1
sums = []
for i in rows:
    s = psolve(i)
    sums.append(s)
print(sum(sums)) # 18.2