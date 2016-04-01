import json
fin = open('result.txt')
data = fin.readlines()
fin.close()
with open(r'..\Cheng\diff_process\json\antlr3_cs_new.json') as data_file:
    javadata = dict(json.load(data_file))

with open(r'..\Cheng\diff_process\json\antlr3_java_new.json') as data_file:
    csdata = dict(json.load(data_file))

for l in data:
	cs, java = l.strip().split(',')
	javacode = javadata[java.split('_')[1]]['code']
	javafn = javadata[java.split('_')[1]]['fname']
	cscode = csdata[cs.split('_')[1]]['code']
	csfn = csdata[cs.split('_')[1]]['fname']
	print "java:", javafn
	for l in javacode:
		print l
	print "csharp:", csfn
	for l in cscode:
		print l
	a = input()