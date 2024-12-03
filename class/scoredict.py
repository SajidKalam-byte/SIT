t1={"player1":30,"player2":40,"player3":35}
t2={"player4":70,"player5":25,"player6":28, "player7":12}
t3={"player8":60, "player9":35, "player10": 40}
t4={}
max1=0
pl=''
for i in t1.keys():
    if t1[i]>max1:
        max1=t1[i]
        pl=i

t4[pl]=max1

max1=0
pl=''
for i in t2.keys():
    if t2[i]>max1:
        max1=t2[i]
        pl=i
        t4[i]=t2[i]
t4[pl]=max1
max1=0
pl=''
for i in t3.keys():
    if t3[i]>max1:
        max1=t3[i]
        pl=i
        t4[i]=t3[i]
t4[pl]=max1

print("\nTop scorer from different team", t4)
