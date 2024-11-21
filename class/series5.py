'''
1   0   1   0   1   0   1
    1   0   1   0   1   
        1   0   1
            1
'''
for i in range(7,0,-2):
    for k in range(i,7):
        print(' ',end='')
    for j in range(i,0,-1):
        if j%2==0:
            print(0,end=' ')
        else:
            print(1, end=' ')
    print()
