log = dict()
f = open("inputd15", "r")
row = f.readline().split(",")
row = [int(i) for i in row]
f.close()
many = 30000000 # many = 2020 in 15.1, 30000000 in 15.2
said = row[len(row) - 1]
for i in range(len(row)):
    log[row[i]] = i
log.popitem()
for i in range(len(row), many):
    if said not in log.keys():
        log[said] = i - 1
        said = 0
    else:
        ex = said
        said = i - log.get(said) - 1
        log[ex] = i - 1
print(said) # 15.1 & 15.2
# slow for 15.2 but still less than 30sec