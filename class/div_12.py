'''Print a series of all numbers between 100 and 700 which are divisible by 12'''
i=100
for i in range(100,700+1):
    if i%12==0:
        print(i,end=" ")