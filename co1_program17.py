d={0:3,1:8,2:4,3:9,4:7,5:2}
l=list(d.items())
l.sort()
d1=dict(l)
print("ascending order is:",d1)
l=list(d.items())
l.sort(reverse=True)
d1=dict(l)
print("descending is:",d1)