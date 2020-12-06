forms = []
form = set()
f = open("inputd06", "r")
for x in f:
    if x == "\n":
        forms.append(len(form))
        form = set()
    line = list(x)
    for y in line:
        if y != "\n":
            form.add(y)
forms.append(len(form))
print(sum(forms)) # 06.1
f.seek(0)
forms = []
form = dict()
c = 0
for x in f:
    if x == "\n":
        s = set()
        for z in form.keys():
            if form[z] == c:
                s.add(z)
        forms.append(len(s))
        c = 0
        form = dict()
    else:
        line = list(x)
        c += 1
        for y in line:
            if y != "\n":
                now = form.get(y, 0)
                form[y] = now + 1
f.close()
s = set()
for z in form.keys():
    if form[z] == c:
        s.add(z)
forms.append(len(s))
print(sum(forms)) # 06.2