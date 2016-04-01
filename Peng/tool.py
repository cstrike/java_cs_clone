import math
"""
fin = open(r'.\data\antlr3\f_d.txt')
fout = open(r'.\data\antlr3\f_d1.txt', 'w')
l = fin.readline()
while l.strip() != '':
    t = l.strip().strip('(').strip(')').replace(' ', '').replace("'", '')
    fout.write(t+'\n')
    l = fin.readline()
fout.close()
fin.close()

exit()
"""
"""
fin = open(r'.\data\antlr3\distance.txt')
fout = open(r'.\data\antlr3\f_d.txt', 'w')
l = fin.readline()
k = 0
while l.strip() != '':
    t = l.strip().strip('(').strip(')').split(',')
    fn1 = t[0]
    fn2 = t[1]
    s1 = float(t[7])
    s2 = float(t[8])
    if fn1[:3] == "'cs":
        if (math.fabs(s1 - s2) / (s1 + s2) <= 0.3333333333):
            fout.write(l)
    l = fin.readline()
fout.close()
fin.close()
exit()

"""

dic = {}
with open(r'.\data\antlr3\f_d1.txt') as fin:
    for l in fin:
        cs, java, timedf, audf, fndf, comdf, codedf, cslen, javalen = l.strip().split(',')
        if fndf == '0':
            try:
                dic[java].append(l)
            except:
                dic[java] = [l]

for key in dic:
    fout = open(r'.\data\antlr3\sp\%s.txt' % key, 'w')
    for l in dic[key]:
        fout.write(l)
    fout.close()