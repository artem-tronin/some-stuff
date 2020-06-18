d = {}
f = open("input.txt", 'r')
for i in f:
    rte = i.split()
    if rte[0] not in d.keys():
        d[rte[0]] = 0
    d[rte[0]]+=int(rte[1])
for i in sorted(d.keys()):
    print(i, d[i])
f.close()