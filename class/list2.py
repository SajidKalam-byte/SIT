l=list()
print(l)
l1=[1,2,3]
l2=[3,4,5]

l3=l1+l2
print(l3)
for i in l3:
    print(i, end=' ')
print()

l5=[10,20,30,40]
l5.append(50)
print(l5)
l5.append(['s','q'])
print(l5)

l5.extend([100,200])
print(l5)

a=[10,20,30,40]
a.insert(2,"new")
print(a)

print(a.index('new'))

print(l3.count(3))

s=[12,3,4,1,54]
s.sort()
print(s)
s.sort(reverse = True)
print(s)
s.reverse()
print(s)

la=[1,2,3,4,5,6]
print(la.pop())

la.remove(2)
print(la)

ab=['a','b','c','d',1,2,3,4]
del ab[1]
print(ab)

del ab[3:]
print(ab)

l=[1,2,3,4,5,6,7]
l[0]=100
print(l)
l[1:3]=[500,600]
print(l)


l=[0]*5
print(l)

l2=[0 for i in range(5)]
print(l2)

l2=[[0 for i in range(5)]for j in range (4)]
print(l2)