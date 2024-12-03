s={1,2,3,4,4,5}
print(s)
print(s[1])
s2={2,3,5,6,7,8}

print(s.intersection(s2))

s3=s.union(s2)
print(s3)

s4=s.difference(s2)
print(s4)

s.add(6)
print(s)

s.update(s2)
print(s)