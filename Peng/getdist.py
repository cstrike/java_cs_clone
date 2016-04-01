#!/usr/bin/python
import json
import numpy as np
import sklearn
from sklearn.cluster import DBSCAN
from sklearn import metrics
import math
data = []

def dist(v1, v2):
    import editdistance
    def L1dis(l1, l2):
        dic = {}
        for k in l1:
            dic[k[0]] = k[1]
        for k in l2:
            if k[0] in dic.keys():
                dic[k[0]] = math.fabs(dic[k[0]] - k[1])
            else:
                dic[k[0]] = k[1]
        res = 0
        for k in dic:
            res += dic[k]
        return res
    def tokennum(v):
        res = 0
        for l in v:
            res += l[1]
        return res
        
    timedf = (v1[2] - v2[2]) / 86400
    if v1[4] == v2[4]:
        audf = 0
    else:
        audf = 1
    fndf = int(editdistance.eval(v1[3], v2[3]))
    comdf = L1dis(v1[1], v2[1])
    codedf = L1dis(v1[5], v2[5])
    return (str(v1[0]), str(v2[0]), timedf, audf, fndf, int(comdf), int(codedf), tokennum(v1[5]), tokennum(v2[5]))

with open(r'.\data\antlr3\feature.json') as data_file:
    jsdata = dict(json.load(data_file))

datanum = []
k = 0
for key in jsdata:
    comment = jsdata[key]['comment']
    ts = jsdata[key]['timestamp']
    fname = jsdata[key]['fname']
    author = jsdata[key]['author']
    code = jsdata[key]['code']
    data.append([key, comment, ts, fname, author, code])
    k += 1

for u in data:
    if u[0][:2] == 'cs':
        for v in data:
            if (v[0][:2] == 'ja'):
                print dist(u, v)

exit()

for u in data:
    tmp = []
    for v in data:
        tmp.append(dist(u, v))
    datanum.append(tmp)

npdata = np.array(datanum, dtype=float)

db = DBSCAN(eps=5, min_samples=2, metric = 'precomputed', algorithm = 'auto').fit(npdata)

for i in range(len(db.labels_)):
    print da.labels_[i], data[i]
#print db.labels_
