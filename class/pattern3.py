'''Print
            1
       2       3
    4       5       6
7       8       9       10
'''
num = int(input("Enter rows: "))
c=0
m = num
for i in range(0, num):
    for j in range(0, m):
        print(end=' ')
    m = m - 1
    for j in range(0, i + 1):
        c+=1
        print(c,end=' ')
        
    print()
