#import re
#from functools import reduce

with open('./input.txt', 'r') as file:
    data = [ tuple(int(c) for c in l.split(',')) for l in file.read().splitlines() ]

def get_area(p1, p2):
    return (abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1)

print(max(get_area(p1,p2)
    for i, p1 in enumerate(data)
    for p2 in data[i+1:]
))


def intersects(p1, p2, p3, p4):
    xm1,xM1,ym1,yM1 = min(p1[0], p2[0]), max(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[1], p2[1])
    xm2,xM2,ym2,yM2 = min(p3[0], p4[0]), max(p3[0], p4[0]), min(p3[1], p4[1]), max(p3[1], p4[1])
    return not(xm1 > xM2 or ym1 > yM2 or xM1 < xm2 or yM1 < ym2)


cdata = []
for i in range(len(data)):
    a,b = data[(i-1)%len(data)]
    c,d = data[i]
    e,f = data[(i+1)%len(data)]
    if c>a and f<d:
        cdata.append( (c-1, d-1) )
    if c>a and f>d:
        cdata.append( (c+1, d-1) )
    if c<a and f>d:
        cdata.append( (c+1, d+1) )
    if c<a and f<d:
        cdata.append( (c-1, d+1) )
    if d>b and e>c:
        cdata.append( (c+1, d-1) )
    if d>b and e<c:
        cdata.append( (c+1, d+1) )
    if d<b and e<c:
        cdata.append( (c-1, d+1) )
    if d<b and e>c:
        cdata.append( (c-1, d-1) )

def ok(p1, p2):
    for i, start in enumerate(cdata):
        end = cdata[(i+1)%len(cdata)]
        if intersects(p1, p2,start, end):
            return False
    return True

print(max(get_area(p1,p2)
    for i, p1 in enumerate(data)
    for p2 in data[i+1:]
    if ok(p1, p2)
))

print("Done.")
