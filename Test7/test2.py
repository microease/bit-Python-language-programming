# coding:utf-8


f = open('data.csv','r')
lines = f.readlines()
lines.reverse()

for line in lines:
    line = line.replace('\n','')
    t = line.split(",")

for line in lines:
    line = line.replace('\n','')
    line =line.replace(' ','')
    t = line.split(",")
    t.reverse()
    print(";".join(t))
