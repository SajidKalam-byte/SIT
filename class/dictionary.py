# d={"Hello" : 1, "World" : 2, 3: [10,20,30], 4: {5: 'a', 6: 'b'}}
# print(d)
# print(d["Hello"])
# print(d[3])
# print(d[3][0])
# print(d[4][5])
# print(d[4][6])

# print(d.items())
# print(d.keys())
# print(d.values())
# d[3]="World"
# print(d[3])
# print(d.items())

# d1={}
# d1[1]='hello'
# d1[2]='world'
# d1['key1']=101
# print(d1.items())

# d2=dict()
# roll=[1,2,3,4]
# name=['sajid','abhay','habib','priyanaka']
# d2=dict(zip(roll,name))
# print(d2.items())
# print(d2)

# for i in d2.keys():
#     print(i)

# for i in d2.values():
#     print(i)

# for i in d2.items():
#     print(i)

# sum=0
# score={'pl1': 100, 'pl2':80, 'pl3':72, 'pl4': 85, 'pl5': 30, 'pl6': 102}
# for i in score.values():
#     sum+=i
# print("Total Score = ",sum)

max=0
score={'pl1': 100, 'pl2':80, 'pl3':72, 'pl4': 85, 'pl5': 130, 'pl6': 102}
for i in score.values():
    if i>max:
        max=i
print("Maximum Score is ", max)
for i in score.keys():
     if i==max:
        max=i
print("Maximum Score is ", max)
# pl=''
# max=0
# score={'pl1': 100, 'pl2':80, 'pl3':72, 'pl4': 85, 'pl5': 130, 'pl6': 102}
# for i in score.keys():
#     if score[i]>max:
#         max=score[i]
#         pl=i
# print(pl, " scored ", max)