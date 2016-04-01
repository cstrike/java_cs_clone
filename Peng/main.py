#!/usr/bin/python
import os
def ls(rootDir):
    list_dirs = os.walk(rootDir)
    tmp = []
    for root, dirs, files in list_dirs:
        for f in files:
            if (f.split('.')[-1] == 'txt'):
                tmp.append( os.path.join(root, f) )

    return tmp

files = ls(r".\data\antlr3\sp")
result = []
for f in files:
    fin = open(f)
    data = fin.readlines()
    tmp = []
    mm = 0

    for l in data:
        t = l.strip().split(',')
        if t[4] == '0':
            tmp.append(l.strip().split(','))
    if len(tmp) == 0:
        continue
    tmp = sorted(tmp, key=lambda x: (x[6]))
    mm = tmp[0][6]
    result.append((tmp[0][0], tmp[0][1]))
    for l in tmp[1:]:
        if (l[6] == mm):
            result.append( (l[0], l[1]) )
        else:
            break
    fin.close()

fout = open('result.txt', 'w')
for t in result:
    fout.write("%s,%s\n" % (t[0], t[1]))
fout.close()