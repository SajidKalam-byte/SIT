s1 ='mca'
print('m' in s1)

s='MCA 1ST SEM'
print(s[2:-1])

print(s[2:9:2])
print(s[0])
print(len(s))
print(s[:-1])
print(s[-1])


str="MCA, hewf jhe"
for i in range(len(str)):
    print(str.partition(sep=', '))