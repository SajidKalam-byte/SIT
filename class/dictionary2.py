i1={'pl1':20, 'pl3':60, 'pl4':32}
i2={'pl1':38, 'pl2':52, 'pl3':40}
i3={'pl2': 35, 'pl3':40, 'pl4': 25}
i4={}
for i in i1.keys():
    i4[i]=i1[i]

for i in i2.keys():
    if i in i4.keys():
        i4[i]=i4[i]+i2[i]
    else:
        i4[i]=i2[i]


for i in i3.keys():
    if i in i4.keys():
        i4[i]=i4[i]+i3[i]
    else:
        i4[i]=i3[i]
print("The total score of all player is ",i4)